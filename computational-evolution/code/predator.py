"""Predator Module"""

from agent import Agent
import matplotlib.patches as patches
from CONSTANTS import *
import numpy as np


class Predator(Agent):
    def __init__(self, pos, speed=None, size=None, energy=None, theta=None):
        super().__init__(pos, speed, size, energy, theta)
        self.patch = patches.Circle(self.pos, self.size, fc='red')
        self.vision_patch = patches.Wedge(self.pos, self.radius,
                                          theta1=(180 / np.pi) * (self.direction - self.angle / 2),
                                          theta2=(180 / np.pi) * (self.direction + self.angle / 2), alpha=0.3,
                                          fc='lightcoral')
