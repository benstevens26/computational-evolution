"""Food Module

Classes:
    Food

Functions:
    None
    
"""

import numpy as np
import matplotlib.patches as patches
from CONSTANTS import *


class Food:
    """Food Class
    
    Attributes:
        pos (array): Position of food
        patch (matplotlib object): Representation of food for animation
        energy (int): Energy of food

    """   
    def __init__(self, pos):
        """Initialise food

        """

        if isinstance(pos, list):
            pos = np.asarray(pos)

        self.pos = pos
        self.size = FOOD_SIZE
        self.energy = EAT_ENERGY
        self.patch = patches.Circle(self.pos, self.size, fc='r')

    def get_pos(self):
        """Return food position"""
        return self.pos

    def get_size(self):
        """Return food size"""
        return self.size

    def get_id(self):
        """Return agent unique id"""
        return id(self)
    
    def get_patch(self):
        """Return patch object"""
        return self.patch

    def get_energy(self):
        """Return food energy"""
        return self.energy
    
    def set_pos(self, new_pos):
        """Set food position"""
        if isinstance(new_pos, list):
            new_pos = np.asarray(new_pos)
        
        self.pos = new_pos

    def update_patch(self):
        """Update patch attribute centre"""
        self.patch.center = self.pos

    def remove_patch(self):
        """Remove patch attribute"""
        self.patch.set_visible(False)
