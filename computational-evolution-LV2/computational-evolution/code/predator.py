"""Predator Module"""

from agent import Agent
import matplotlib.patches as patches
from CONSTANTS import *
import numpy as np


class Predator(Agent):
    def __init__(self, pos, speed=None, size=None, energy=None, theta=None):

        size = 100
        speed = 90
        theta = np.pi/5

        super().__init__(pos, speed, size, energy, theta)

        self.energy = 20000

        self.patch = patches.Circle(self.pos, self.size, fc='red')
        self.vision_patch = patches.Wedge(self.pos, self.radius,
                                          theta1=(180 / np.pi) * (self.direction - self.angle / 2),
                                          theta2=(180 / np.pi) * (self.direction + self.angle / 2), alpha=0.3,
                                          fc='lightcoral')

    def eat_food(self, food):
        """Increase agent energy by energy of prey"""
        eat_energy = 1.5 * EAT_ENERGY
        # eat_energy = 0.8 * EAT_ENERGY
        new_energy = self.get_energy() + eat_energy
        if new_energy > PREDATOR_MAX_ENERGY:
            new_energy = PREDATOR_MAX_ENERGY
        self.set_energy(new_energy)

    def get_energy_loss(self):
        """Return energy loss per step"""
        t = TIME_STEP
        energy_loss = ((t * self.speed * self.speed) / 1000000) * (self.size * self.size)
        return energy_loss

    def move(self):
        """Move agent one step, update position, decrease energy"""

        t = TIME_STEP
        dx, dy = self.rand_walk(t)  # generate dx, dy for random walk
        self.pos += np.asarray([dx, dy])

        new_energy = self.energy - self.get_energy_loss()
        self.set_energy(new_energy)


