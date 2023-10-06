

import numpy as np
from agent import Agent

class Environment:
    def __init__(self, size: int, num_agents, agent_speed, num_food):
        '''Initialise the environment
        
        Arguments:

        size - integer side length of square environment in m

        num_agents - number of agents to place randomly within environment

        agent_speed - speed of agents in ms^-1

        num_food - number of food items to place randomly within environment (and maintain)
        '''

        self.size = size
        self.num_agents = num_agents
        self.agent_speed = agent_speed
        self.num_food = num_food

    def addAgent(self):
        '''place an agent into the environment'''
        agent = Agent(pos=[0,np.random.randint(0, self.size)], speed=self.agent_speed)

    def add_food(self):
        '''add food into the environment'''

    def
        
        

        





