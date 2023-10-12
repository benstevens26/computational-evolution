"""Agent Module

Classes:
    Agent

Functions:
    None

"""

import numpy as np
import matplotlib.animation as animation
import matplotlib.patches as patches
from CONSTANTS import *

class Agent:
    """Agent class
    
    Attributes:
        pos (array): Position of agent
        speed (float): Speed of agent in ms^-1
        energy (float): Energy of agent in J
        patch (matplotlib object): Representation of agent for animation
        direction (float): Direction of agent

    Methods:
        pos(): Return agent position
        setPos(new_pos): Set agent position
        speed(): Return agent speed
        energy(): Return agent energy
        setEnergy(new_energy): Set agent energy
        patch(): Return patch object
        eat(): Increase agent energy by EAT_ENERGY (see CONSTANTS.py)
        id(): Return agent unique id
        randWalk(t): Return dx, dy for a correlated random walk
        move(t): Move agent by time t (in s) using randWalk() 
        updatePatch(): Update patch attribute centre

    """
    def __init__(self, pos):
        """Initialise agent
        
        Parameters:
            pos (list/array): initial position [x,y]
        """

        if type(pos) == type(list): # ensure vectorised
            pos = np.asarray(pos)

        self.pos = pos # assign position, speed, energy, and direction 
        self.speed = INIT_SPEED
        self.energy = INIT_ENERGY
        self.direction = np.random.uniform(-np.pi, np.pi)
        self.patch = patches.Circle(pos, AGENT_SIZE, fc='g')

    def pos(self):
        """Return agent position"""
        return self.pos

    def setPos(self, new_pos):
        """Set agent position"""
        if type(new_pos) == type(list): # ensure vectorised
            new_pos = np.asarray(new_pos)
        
        self.pos = new_pos
    
    def speed(self):
        """Return agent speed"""
        return self.speed
    
    def energy(self):
        """Return agent energy"""
        return self.energy
    
    def setEnergy(self, new_energy):
        """Set agent energy"""
        self.energy = new_energy
    
    def patch(self):
        """Return patch object"""
        return self.patch
    
    def eat(self):
        """Increase agent energy by EAT_ENERGY"""
        self.energy += EAT_ENERGY
        if self.energy > MAX_ENERGY: # energy is maximum
            self.energy = MAX_ENERGY

    def id(self):
        """Return agent unique id"""
        return id(self)
    
    def randWalk(self, t):
        """Return dx, dy for a correlated random walk"""

        cone = np.pi / 4  # half the angle of a cone
        correlation = CORRELATION_FACTOR 

        new_direction = self.direction + np.random.uniform(-cone, cone)
        self.direction = correlation * new_direction + (1-correlation) * self.direction

        delta_x = self.speed * t * np.cos(self.direction)
        delta_y = self.speed * t * np.sin(self.direction)

        new_pos = self.pos + np.asarray([delta_x, delta_y])

        if new_pos[0] <= 0 or new_pos[0] >= ENV_SIZE: # out of x boundary
            self.direction = np.pi - self.direction
            delta_x = self.speed * t * np.cos(self.direction)

        elif new_pos[1] <= 0 or new_pos[1] >= ENV_SIZE: #out of y boundary
            self.direction = -self.direction
            delta_y = self.speed * t * np.sin(self.direction)

        return delta_x, delta_y

    def move(self, t):
        """Move agent by time t using randWalk() and decrease agent energy"""

        dx, dy = self.randWalk(t) # generate dx, dy
        self.pos += np.asarray([dx, dy]) # update position

        energy_loss = t * self.speed * self.speed
        self.energy = self.energy - energy_loss # update energy

    def updatePatch(self):
        """Update patch attribute centre"""
        self.patch.center = self.pos

    def removePatch(self):
        """Remove patch attribute"""
        self.patch.center = np.asarray([500, 500]) # for testing




        




