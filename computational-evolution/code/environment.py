"""Environment Module

Classes:
    Environment

Functions:
    None
    
"""
import random

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
from CONSTANTS import *
from agent import Agent
from food import Food
import pandas as pd


class Environment:
    """Environment Class
    
    Attributes:
        size (int): size of environment walls in m
        num_agents (int): number of agents in the environment
        num_food (int): number of food objects in the environment
        time_elapsed (float): time elapsed in seconds
        agent_list (list): list of agent objects
        food_list (list): list of food objects

    Methods:
        genPos(): Generate a random position within environment
        addAgent(): Add agent into environment
        getAgent(id): Return agent with a given id
        addFood(): Add food into environment
        populate(): Populate the environment with agents and food
        eatCheck(agent): Check for food nearby agent and eat()
        step(): Step a set time through the environment
        animate(): Animate environment using matplotlib 
        run(animate): Run simulation for NUM_FRAMES, option to animate
        recordagents(): Record the position, IDs and energies of agents for each time step
        recordpop(): Record the number of food and agents as simulation runs
        recordfood(): Record the position and ID of food for each time step

    """

    def __init__(self):
        """Initialise environment
        
        Parameters:
            None

        """

        self.size = ENV_SIZE
        self.time_elapsed = 0
        self.num_agents = 0
        self.num_food = 0

        self.agent_list = []  # create agent and food lists
        self.food_list = []

        self.agent_data = []
        self.food_data = []

        # Dataframes for data storage
        self.agent_df = pd.DataFrame(columns=['Time Elapsed/s', 'ID', 'X-Coord', 'Y-Coord', 'Energy'])
        self.pop_df = pd.DataFrame(columns=['Time Elapsed/s', 'Agent Population', 'Food Population'])
        self.food_df = pd.DataFrame(columns=['Time Elapsed', 'ID', 'X-Coord', 'Y-Coord'])

    def genPos(self):
        """Return a random position within environment"""
        x = np.random.uniform(0, ENV_SIZE)
        y = np.random.uniform(0, ENV_SIZE)
        return np.asarray([x, y])

    def addAgent(self, init_pos=None):
        """Add agent into environment"""

        if init_pos is None:  # when pos not given
            init_pos = self.genPos()

        self.agent_data = []

        agent = Agent(init_pos)
        self.agent_list.append(agent)
        self.agent_data.append(agent)
        self.num_agents = int(self.num_agents + 1)

        if ANIMATE == True:
            self.axes.add_patch(Agent.patch(agent))

    def getAgent(self, id):
        """Return agent with a given id"""
        for agent in self.agent_list:
            if Agent.id(agent) == id:
                return agent

    def addFood(self):
        """Add food into environment"""

        init_pos = self.genPos()
        food = Food(init_pos)

        self.food_list.append(food)
        self.food_data.append(food)
        self.num_food = int(self.num_food + 1)

        if ANIMATE == True:
            self.axes.add_patch(Agent.patch(food))

    def populate(self):
        """Populate the environment with agents and food"""

        for i in range(0, INIT_NUM_AGENTS):
            self.addAgent()
        for i in range(0, INIT_NUM_FOOD):
            self.addFood()

    def eatCheck(self, agent):
        """Check for food nearby agent and eat()"""

        del_list_food = []
        for food in self.food_list:
            if np.linalg.norm(Agent.pos(agent) - Food.pos(food)) < AGENT_SIZE:
                Food.removePatch(food)  # remove food patch
                del_list_food.append(food)

                self.num_food = self.num_food - 1
                Agent.eat(agent)

        self.food_list = [food for food in self.food_list if food not in del_list_food]

    def reproduce(self, parent):
        """Check for nearby eligible agent and produce offspring"""

        if self.num_agents > 1:
            for agent in self.agent_list:
                if agent != parent and Agent.energy(agent) > REP_THRESHOLD * MAX_ENERGY:
                    distance = np.linalg.norm(Agent.pos(parent) - Agent.pos(agent))  # Calculates distance between
                    # two eligible agents

                    if distance < AGENT_SIZE:
                        chosen_parent = random.choice([agent, parent])  # Randomly chooses a parent
                        child_pos = Agent.pos(chosen_parent) + np.random.uniform(-0.1, 0.1, 2)
                        new_energy = Agent.energy(chosen_parent) - INIT_ENERGY  # energy of parent decreases by new
                        # energy of child
                        Agent.setEnergy(chosen_parent, new_energy)

                        self.addAgent(init_pos=child_pos)

    def divide(self, parent):
        """Duplicate agent"""

        child_pos = Agent.pos(parent) + np.asarray([0.1, 0.1])
        new_energy = Agent.energy(parent) - INIT_ENERGY  # energy of parent decreases by new energy of child
        Agent.setEnergy(parent, new_energy)

        self.addAgent(init_pos=child_pos)

    def step(self):
        """Step a set time through the environment"""

        if self.num_agents == 0:
            raise Exception("No agents remaining -> stopping simulation")

        t = TIME_STEP  # simulation time between steps
        self.time_elapsed += t

        del_list_agent = []
        for agent in self.agent_list:
            self.agent_data = []  # reset to ensure duplicate data not added to df

            Agent.move(agent, t)
            self.eatCheck(agent)

            self.agent_data.append(agent)

            if Agent.energy(agent) < 0:  # death
                Agent.removePatch(agent)
                del_list_agent.append(agent)
                self.num_agents = int(self.num_agents - 1)

            if Agent.energy(agent) > REP_THRESHOLD * MAX_ENERGY:  # division/reproduction
                self.divide(parent=agent)

        self.agent_list = [agent for agent in self.agent_list if agent not in del_list_agent]

        p = FOOD_SPAWN_RATE  # natural food addition rate per time step
        r = np.random.uniform(0.0, 1.0)

        if r <= p:
            self.addFood()

    def recordState(self):
        """Record all information about state"""
        #self.recordagents()
        #self.recordfood()
        self.recordpop()

    def animate(self, i):
        """Animate environment using matplotlib"""

        self.step()
        self.time_text.set_text('Time: {:.1f}'.format(self.time_elapsed))
        self.pop_text.set_text('Population: {:.0f}'.format(self.num_agents))

        for agent in self.agent_list:
            Agent.updatePatch(agent)

        for food in self.food_list:
            Food.updatePatch(food)

    def run(self):
        """Run simulation for NUM_FRAMES"""

        if ANIMATE == True:
            self.fig = plt.figure('Environment', figsize=(6, 6))
            self.axes = plt.axes(xlim=(0, ENV_SIZE), ylim=(0, ENV_SIZE))

            self.time_text = self.axes.text(0.4 * ENV_SIZE, 1.02 * ENV_SIZE, '')
            self.pop_text = self.axes.text(0.4 * ENV_SIZE + 10, 1.02 * ENV_SIZE, '')

            self.populate()

            anim = animation.FuncAnimation(self.fig, self.animate, frames=NUM_FRAMES, repeat=False,
                                           interval=10)  # 10x speed
            plt.show()

        else:
            self.populate()
            for i in range(0, NUM_FRAMES):
                self.step()
                if int(i/25) == i/25:
                    self.recordState()
                print('frame',i)

            num = np.random.randint(0, 100000)
            self.agent_df.to_csv(
                f"computational-evolution/Data/Agent_Data_{num}.csv",
                index=False)
            self.pop_df.to_csv(
                f"computational-evolution/Data/Population_Data_{num}.csv",
                index=False)
            self.food_df.to_csv(
                f"computational-evolution/Data/Food_Data_{num}.csv", index=False)

    def recordagents(self):
        """Record the position, IDs and energies of agents for each time step"""

        for i in self.agent_data:  # Extracts information from agent list
            pos = Agent.pos(i)
            energy = Agent.energy(i)
            i_d = Agent.id(i)

            self.agent_df.loc[len(self.agent_df)] = [self.time_elapsed, i_d, pos[0], pos[1], energy]

    def recordpop(self):
        """Record the number of food and agents as simulation runs"""

        self.pop_df.loc[len(self.pop_df)] = [self.time_elapsed, self.num_agents, self.num_food]

    def recordfood(self):
        """Record the position and ID of food for each time step"""

        for f in self.food_data:
            pos = Food.pos(f)
            i_d = Food.id(f)

            self.food_df.loc[len(self.food_df)] = [self.time_elapsed, i_d, pos[0], pos[1]]
