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
        removePatch(): Remove patch attribute

    """

    def __init__(self, pos, speed=None):
        """Initialise agent
        
        Parameters:
            pos (list/array): initial position [x,y]
            speed (int): initial speed
        """

        if type(pos) == type(list):  # ensure vectorised
            pos = np.asarray(pos)

        if speed is None:
            self.speed = np.random.randint(50, 150)  # initiate agents with integer speed between 50-150
        else:
            self.speed = speed

        self.pos = pos  # assign position, energy, and direction
        self.energy = INIT_ENERGY
        self.direction = np.random.uniform(-np.pi, np.pi)
        self.patch = patches.Circle(pos, AGENT_SIZE, fc='g')

    def pos(self):
        """Return agent position"""
        return self.pos

    def setPos(self, new_pos):
        """Set agent position"""
        if type(new_pos) == type(list):  # ensure vectorised
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
        if self.energy > MAX_ENERGY:  # energy is maximum
            self.energy = MAX_ENERGY

    def id(self):
        """Return agent unique id"""
        return id(self)

    def randWalk(self, t):
        """Return dx, dy for a correlated random walk"""

        cone = np.pi / 4  # half the angle of a cone
        correlation = CORRELATION_FACTOR

        new_direction = self.direction + np.random.uniform(-cone, cone)
        self.direction = correlation * new_direction + (1 - correlation) * self.direction

        delta_x = self.speed * t * np.cos(self.direction)
        delta_y = self.speed * t * np.sin(self.direction)

        new_pos = self.pos + np.asarray([delta_x, delta_y])

        if not 0 < new_pos[0] <= ENV_SIZE:
            new_pos[0] = new_pos[0] % ENV_SIZE
            delta_x = new_pos[0] - self.pos[0]

        if not 0 < new_pos[1] <= ENV_SIZE:
            new_pos[1] = new_pos[1] % ENV_SIZE
            delta_y = new_pos[1] - self.pos[1]

        return delta_x, delta_y

    def move(self):
        """Move agent using randWalk() and decrease agent energy"""

        t = TIME_STEP
        dx, dy = self.randWalk(t)  # generate dx, dy
        self.pos += np.asarray([dx, dy])  # update position

        energy_loss = t * self.speed
        self.energy = self.energy - energy_loss  # update energy

    def updatePatch(self):
        """Update patch attribute centre"""
        self.patch.center = self.pos

    def removePatch(self):
        """Remove patch attribute"""
        self.patch.set_visible(False)
