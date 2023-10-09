import numpy as np
from food import Food
from agent import Agent

class Environment:
    def __init__(self, size: int, agent_speed):
        '''Initialise a static environment
        
        includes methods for instantiating agents and food

        Arguments:

        size - integer side length of square environment in m

        agent_speed - speed of agents in ms^-1
        '''

        self.size = size
        self.agent_speed = agent_speed

    def addAgent(self):
        '''place an agent into the environment'''
        return Agent(pos=[np.random.uniform(0, self.size), np.random.uniform(0, self.size)], speed=self.agent_speed)
        
    def addFood(self):
        '''add food into the environment'''
        return Food(pos=[np.random.uniform(0, self.size), np.random.uniform(0, self.size)])


        

     