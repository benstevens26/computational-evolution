import numpy as np

class Food:
    def __init__(self, pos):
        '''Initialise food

        Arguments:

        pos - list or numpy array containing initial position e.g. [0,0]
        '''

        if type(pos) == type(list):
            pos = np.asarray(pos)

        self.pos = pos

    def pos(self):
        '''return food position'''
        return self.pos
