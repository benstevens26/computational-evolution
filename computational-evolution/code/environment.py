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
        steps (int): number of steps elapsed
        agent_list (list): list of agent objects
        food_list (list): list of food objects

    Methods:
        genPos(): Generate a random position within environment
        addAgent(): Add agent into environment
        getAgent(id): Return agent with a given id
        addFood(): Add food into environment
        populate(): Populate the environment with agents and food
        eatCheck(agent): Check for food nearby agent and eat()
        divide(parent): Create a copy of the parent
        mutate(parent): Allow for mutation to occur during divide method
        step(): Step a set time through the environment
        animate(): Animate environment using matplotlib 
        run(animate): Run simulation for NUM_FRAMES, option to animate
        recordAgents(): Append data for each agent instance to agent_data
        recordPop(): Append population data to pop_data
        recordFood(): Append data for each food instance to food_data
        saveData(): Package all data into dataframe and save csv files to /data

    """

    def __init__(self, size=ENV_SIZE, sim_num=1):
        """Initialise environment
        
        Parameters:
            size(int) = length of a 'wall' of the environment
            sim_num(int) = simulation number

        """

        self.size = size
        self.steps = 0
        self.num_agents = 0
        self.num_food = 0
        self.sim_num = sim_num

        self.agent_list = []  # create agent and food lists
        self.food_list = []

        self.food_data = []  # data lists
        self.agent_data = []
        self.pop_data = []
        self.mutation_count = 0

    def genPos(self):
        """Return a random position within environment"""

        x = np.random.uniform(0, ENV_SIZE)
        y = np.random.uniform(0, ENV_SIZE)
        return np.asarray([x, y])

    def addAgent(self, init_pos=None, init_speed=None, init_size=None):
        """Add agent into environment"""

        if init_pos is None:  # when pos not given
            init_pos = self.genPos()

        agent = Agent(init_pos, init_speed) # , init_size)
        self.agent_list.append(agent)
        self.num_agents = int(self.num_agents + 1)

        if ANIMATE is True:
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
        self.num_food = int(self.num_food + 1)

        if ANIMATE is True:
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
            if np.linalg.norm(Agent.pos(agent) - Food.pos(food)) < (AGENT_SIZE + FOOD_SIZE): # (Agent.size(agent) + FOOD_SIZE):
                Food.removePatch(food)  # remove food patch
                del_list_food.append(food)

                self.num_food = int(self.num_food - 1)
                Agent.eat(agent)

        self.food_list = [food for food in self.food_list if food not in del_list_food]  # new food list

    def reproduce(self, parent):
        """Check for nearby eligible agent and produce offspring"""

        if self.num_agents > 1:
            for agent in self.agent_list:
                if agent != parent and Agent.energy(agent) > REP_THRESHOLD * MAX_ENERGY:
                    # calculate distance between eligible agents
                    distance = np.linalg.norm(Agent.pos(parent) - Agent.pos(agent))

                    if distance < AGENT_SIZE:
                        chosen_parent = random.choice([agent, parent])  # Randomly chooses a parent
                        child_pos = Agent.pos(chosen_parent) + np.random.uniform(-0.1, 0.1, 2)
                        new_energy = Agent.energy(chosen_parent) - INIT_ENERGY  # energy of parent decreases by new
                        # energy of child
                        Agent.setEnergy(chosen_parent, new_energy)

                        self.addAgent(init_pos=child_pos)

    def divide(self, parent):
        """Duplicate agent"""

        child_pos = Agent.pos(parent) + np.asarray([0.01, 0.01])
        new_energy = Agent.energy(parent) - INIT_ENERGY  # energy decrease
        speed = self.mutate(parent)

        Agent.setEnergy(parent, new_energy)
        self.addAgent(init_pos=child_pos, init_speed=speed) # , init_size=size)

    def mutate(self, parent):
        """Mutate speed of offspring"""

        if np.random.random() < PROB_MUTATE:  # alter speed of offspring by sampling from Poisson distribution
            #mutation = np.random.choice(['size', 'speed'])
            self.mutation_count += 1

          #  if mutation == 'speed':
            speed = Agent.speed(parent) + (np.random.poisson(5, None) + 1) * (np.random.choice([-1, 1]))
            if speed < 0:
                speed = 0
                # size = Agent.size(parent)

          #  elif mutation == 'size':
              #  size = Agent.size(parent) + (np.random.poisson(2, None) + 1) * (np.random.choice([-1, 1]))
              #  speed = Agent.speed(parent)

        else:
            speed = Agent.speed(parent)
            #size = Agent.size(parent)

        return speed #, size

    def step(self):
        """Step a set time through the environment"""

        if self.num_agents == 0:
            self.saveData()
            raise Exception("No agents remaining -> stopping simulation")

        del_list_agent = []
        for agent in self.agent_list:

            Agent.move(agent)
            self.eatCheck(agent)

            if Agent.energy(agent) < 0:  # remove dead agents
                Agent.removePatch(agent)
                del_list_agent.append(agent)
                self.num_agents = int(self.num_agents - 1)

            if Agent.energy(agent) > (REP_THRESHOLD * MAX_ENERGY):  # division/reproduction
                self.divide(parent=agent)

        self.agent_list = [agent for agent in self.agent_list if agent not in del_list_agent]

        r = np.random.uniform(0.0, 1.0)
        if r <= FOOD_SPAWN_RATE:
            self.addFood()  # base food spawn rate

        self.steps += 1

    def animate(self, i):
        """Animate environment using matplotlib"""

        self.step()
        self.step_text.set_text('Steps: ' + str(self.steps))
        self.pop_text.set_text('Population: ' + str(self.num_agents))

        for agent in self.agent_list:
            Agent.updatePatch(agent)

        for food in self.food_list:
            Food.updatePatch(food)

    def run(self, data='all'):
        """Run simulation for NUM_FRAMES"""

        if ANIMATE is True:
            self.fig = plt.figure('Environment', figsize=(6, 6))
            self.axes = plt.axes(xlim=(0, ENV_SIZE), ylim=(0, ENV_SIZE))

            self.step_text = self.axes.text(0.4 * ENV_SIZE, 1.02 * ENV_SIZE, '')
            self.pop_text = self.axes.text(0.6 * ENV_SIZE, 1.02 * ENV_SIZE, '')

            self.populate()

            anim = animation.FuncAnimation(self.fig, self.animate, frames=NUM_STEPS, repeat=False,
                                           interval=10)  # 10x speed
            plt.show()

        else:
            if data == 'none':
                self.populate()

                for i in range(0, NUM_STEPS):
                    self.step()

            elif data == 'all':
                self.populate()

                for i in range(0, NUM_STEPS):

                    if int(i / DATA_INTERVAL) == i / DATA_INTERVAL:
                        self.recordState()

                    self.step()
                    print(i)

                self.saveData()

            elif data == 'agents':
                self.populate()

                for i in range(0, NUM_STEPS):

                    if int(i / DATA_INTERVAL) == i / DATA_INTERVAL:
                        self.recordAgents()

                    self.step()

                self.saveData()

            elif data == 'pop':
                self.populate()

                for i in range(0, NUM_STEPS):

                    if int(i / DATA_INTERVAL) == i / DATA_INTERVAL:
                        self.recordPop()

                    self.step()

                self.saveData()

            else:
                raise Exception('Enter valid option for data')

    def recordAgents(self):
        """Append data for each agent instance to agent_data"""

        for agent in self.agent_list:  # extracts information from agent list
            pos = Agent.pos(agent)
            energy = Agent.energy(agent)
            id = Agent.id(agent)
            speed = Agent.speed(agent)
            #size = Agent.size(agent)

            energy_rounded = np.round(energy, 3)
            x_rounded = np.round(pos[0], 3)
            y_rounded = np.round(pos[1], 3)

            self.agent_data.append([self.steps, id, x_rounded, y_rounded, energy_rounded, speed])

    def recordPop(self):
        """Append population data to pop_data"""

        self.pop_data.append([self.steps, self.num_agents, self.num_food])

    def recordFood(self):
        """Append data for each food instance to food_data"""

        for f in self.food_list:
            pos = Food.pos(f)
            id = Food.id(f)

            x_rounded = np.round(pos[0], 3)
            y_rounded = np.round(pos[1], 3)

            self.food_data.append([self.steps, id, x_rounded, y_rounded])

    def recordState(self):
        """Record all information about state"""
        self.recordAgents()
        self.recordFood()
        self.recordPop()

    def saveData(self):
        """Package all data into dataframe and save csvs to /data"""

        # dataframes 
        agent_df = pd.DataFrame(data=self.agent_data,
                                columns=['Time Elapsed/s', 'ID', 'X-Coord', 'Y-Coord', 'Energy', 'Speed'])
        pop_df = pd.DataFrame(data=self.pop_data,
                              columns=['Time Elapsed/s', 'Agent Population', 'Food Population'])
        food_df = pd.DataFrame(data=self.food_data,
                               columns=['Time Elapsed', 'ID', 'X-Coord', 'Y-Coord'])

        filename = 'base_rate_' + str(BASE_LOSS) + '_' + str(self.sim_num)

        if agent_df.shape[0] > 10:
            agent_df.to_csv(
                f"C:/Users/alyss/OneDrive/Documents/GitHub/computational-evolution/computational-evolution/data"
                f"/Agent_Data_{filename}.csv",
                index=False)

        if pop_df.shape[0] > 10:
            pop_df.to_csv(
                f"C:/Users/alyss/OneDrive/Documents/GitHub/computational-evolution/computational-evolution/data"
                f"/Population_Data_{filename}.csv",
                index=False)

        if food_df.shape[0] > 10:
            food_df.to_csv(
                f"C:/Users/alyss/OneDrive/Documents/GitHub/computational-evolution/computational-evolution/data"
                f"/Food_Data_{filename}.csv",
                index=False)
