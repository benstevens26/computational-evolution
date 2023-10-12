"""Environment Module

Classes:
    Environment

Functions:
    None
    
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
from CONSTANTS import *
from agent import Agent
from food import Food

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

        self.agent_list = [] # create agent and food lists 
        self.food_list = []

    def genPos(self):
        """Return a random position within environment"""
        x = np.random.uniform(0, ENV_SIZE)
        y = np.random.uniform(0, ENV_SIZE)
        return np.asarray([x,y])

    def addAgent(self, init_pos=None):
        """Add agent into environment"""

        if init_pos is None: # when pos not given
            init_pos = self.genPos()

        agent = Agent(init_pos)
        self.agent_list.append(agent)
        self.num_agents += 1

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
            if np.linalg.norm(Agent.pos(agent)-Food.pos(food)) < AGENT_SIZE:

                Food.removePatch(food) #remove food patch 
                del_list_food.append(food)     

                self.num_food = self.num_food - 1
                Agent.eat(agent)

        self.food_list = [food for food in self.food_list if food not in del_list_food]

    def divide(self, parent):
        """Duplicate agent"""

        child_pos = Agent.pos(parent) + np.asarray([0.1, 0.1])
        new_energy = Agent.energy(parent) - INIT_ENERGY # energy of parent decreases by new energy of child
        Agent.setEnergy(parent, new_energy)

        self.addAgent(init_pos = child_pos)
        
    def step(self):
        """Step a set time through the environment"""

        if self.num_agents == 0:
            raise Exception("No agents remaining -> stopping simulation")

        t = TIME_STEP # simulation time between steps
        self.time_elapsed += t
        
        del_list_agent = []
        for agent in self.agent_list:
            Agent.move(agent, t)
            self.eatCheck(agent) 
        
            if Agent.energy(agent) < 0: #death
                Agent.removePatch(agent)
                del_list_agent.append(agent)
                self.num_agents -= 1

            if Agent.energy(agent) > REP_THRESHOLD * MAX_ENERGY: #division
                self.divide(parent=agent)

        self.agent_list = [agent for agent in self.agent_list if agent not in del_list_agent]

        p = FOOD_SPAWN_RATE # natural food addition rate per time step
        r = np.random.uniform(0.0, 1.0)

        if r <= p:
            self.addFood()
            self.num_food += 1
        
    def animate(self, i):
        """Animate environment using matplotlib"""

        self.step()
        
        for agent in self.agent_list:
            Agent.updatePatch(agent)

        for food in self.food_list:
            Food.updatePatch(food)

    def run(self):
        """Run simulation for NUM_FRAMES"""

        if ANIMATE == True:
            self.fig = plt.figure('Environment', figsize=(6, 6))
            self.axes = plt.axes(xlim=(0, ENV_SIZE), ylim=(0, ENV_SIZE))

            self.populate()

            anim = animation.FuncAnimation(self.fig, self.animate, frames=NUM_FRAMES, repeat=False, interval=10)
            plt.show()
        
        else:
            self.populate()
            for i in range(0, NUM_FRAMES):
                self.step()

        


