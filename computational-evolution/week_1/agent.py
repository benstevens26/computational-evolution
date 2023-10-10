import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, pos, speed, ident):
        '''Initialise an organism (agent)
        
        Arguments:

        pos - list or numpy array containing initial position e.g. [0,0]

        speed - speed of agent in ms^-1 e.g. 1, 2.4
        '''

        if type(pos) == type(list):
            pos = np.asarray(pos)

        self.pos = pos
        self.speed = speed
        self.energy = 100
        self.UID = ident


    def pos(self):
        '''return agent position'''
        return self.pos

    def UID(self):
        '''return agent unique identification'''
        return self.UID
    
    def setPos(self, new_pos):
        if type(new_pos) == type(list):
            new_pos = np.asarray(new_pos)

        self.pos = new_pos
    
    def speed(self):
        '''return agent speed'''
        return self.speed
    
    def energy(self):
        '''return agent energy'''
        return self.energy

    def move(self, t):
        '''choose random direction and move t seconds in that direction'''
        theta = np.random.uniform(0, 2 * np.pi)
        dx = self.speed * t * np.sin(theta)
        dy = self.speed * t * np.cos(theta)

        self.pos = self.pos + np.asarray([dx,dy]) #updates position

        self.energy = self.energy - (t * self.speed * self.speed)  # energy loss proportional to t*v^2

    def eat(self):
        '''eat food and reset energy'''
        self.energy = 100



