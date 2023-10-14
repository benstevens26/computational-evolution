"""Food Module

Classes:
    Environment

Functions:
    None
    
"""

import numpy as np
import matplotlib.patches as patches
from CONSTANTS import *

class Food:
    """Food Class
    
    Attributes:
        !ADD ATTRIBUTES!

    Methods:
        !ADD METHODS!

    """   
    def __init__(self, pos):
        """Initialise food
        
        Parameters:
            pos (list/array): initial position [x,y]            

        """

        if type(pos) == type(list):
            pos = np.asarray(pos)

        self.pos = pos
        self.patch = patches.Circle(pos, FOOD_SIZE, fc='r')

    def pos(self):
        """Return food position"""
        return self.pos
    
    def patch(self):
        """Return patch object"""
        return self.patch
    
    def setPos(self, new_pos):
        """Set food position"""
        if type(new_pos) == type(list): # ensure vectorised
            new_pos = np.asarray(new_pos)
        
        self.pos = new_pos

    def updatePatch(self):
        """Update patch attribute centre"""
        self.patch.center = self.pos

    def removePatch(self):
        """Remove patch attribute"""
        self.patch.center = np.asarray([500, 500]) # for testing
