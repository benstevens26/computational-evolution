"""Predator Module"""

from agent import Agent
import matplotlib.patches as patches
from CONSTANTS import *
import numpy as np


class Predator(Agent):
    def __init__(self, pos, speed=None, size=None, energy=None):
        super().__init__(pos, speed, size, energy)
        self.patch = patches.Circle(self.pos, self.size, fc='red')





