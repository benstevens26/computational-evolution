"""Predator Module"""

from agent import Agent
import matplotlib.patches as patches
from CONSTANTS import *
import numpy as np


class Predator(Agent):
    def __init__(self, pos, speed=None, size=None, energy=None):

        if isinstance(pos, list):
            pos = np.asarray(pos)

        if speed is None:
            self.speed = np.random.randint(50, 150)
        else:
            self.speed = speed

        if size is None:
            self.size = np.random.randint(100, 200)
        else:
            self.size = size

        if energy is None:
            self.energy = INIT_ENERGY
        else:
            self.energy = energy

        self.pos = pos
        self.direction = np.random.uniform(-np.pi, np.pi)
        self.rep_threshold = REP_THRESHOLD
        self.patch = patches.Circle(self.pos, self.size, fc='red')





