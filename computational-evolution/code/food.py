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

    Methods:
        pos(): Return food position
        patch(): Return patch object
        setPos(new_pos): Set food position to new_pos
        updatePatch(): Update patch attribute centre
        removePatch(): Remove patch attribute

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

    def id(self):
        """Return agent unique id"""
        return id(self)
    
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
        self.patch.center = np.asarray([500, 500]) # CHANGE this #

