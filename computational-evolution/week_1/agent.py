import numpy as np

class Agent:
    def __init__(self, pos, speed):
        '''Initialise an organism (agent)
        
        Arguments:

        pos - list or array containing initial position e.g. [0,0]

        speed - speed of agent in ms^-1 e.g. 1, 2.4
        '''

        if type(pos) == type(list):
            pos = np.asarray(pos)

        self.pos = pos
        self.speed = speed
        self.energy = 100

    def pos(self):
        '''return agent position'''
        return self.pos
    
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

        if self.pos[0] + dx < 0: #stops movement at wall
            dx = 0
        
        if self.pos[1] + dy < 0:
            dy = 0

        self.pos = self.pos + np.asarray([dx,dy]) #updates position

        self.energy = self.energy - (0.5 * self.speed * self.speed)  #updates energy

        print(self.pos) #currently for testing

    def eat(self):
        '''eat food and reset energy'''
        self.energy = 100



