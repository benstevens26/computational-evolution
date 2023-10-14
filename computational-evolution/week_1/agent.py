import numpy as np
import matplotlib.pyplot as plt

environment = [20,20]

class Agent:
    def __init__(self, pos, speed, ident):
        """Initialise an organism (agent)

        Arguments:

        pos - list or numpy array containing initial position e.g. [0,0]

        speed - speed of agent in ms^-1 e.g. 1, 2.4
        """

        if type(pos) == type(list):
            pos = np.asarray(pos)

        self.pos = pos
        self.speed = speed
        self.energy = 100
        self.UID = ident
        self.direction = np.random.uniform(-np.pi, np.pi)

    def pos(self):
        """return agent position"""
        return self.pos

    def UID(self):
        """return agent unique identification"""
        return self.UID

    def setPos(self, new_pos):
        if type(new_pos) == type(list):
            new_pos = np.asarray(new_pos)

        self.pos = new_pos

    def speed(self):
        """return agent speed"""
        return self.speed

    def energy(self):
        """return agent energy"""
        return self.energy

    def move(self, t):
        """Method for a correlated random walk within the area of a cone"""
        cone = np.pi / 4  # half the angle of a cone
        correlation = 0.8  # correlation factor

        new_direction = self.direction + np.random.uniform(-cone, cone)
        self.direction = correlation * new_direction + (1-correlation) * self.direction

        delta_x = self.speed * t * np.cos(self.direction)
        delta_y = self.speed * t * np.sin(self.direction)

        new_pos = self.pos + np.asarray([delta_x, delta_y])

        if 0 < new_pos[0] < environment[0] and 0 < new_pos[1] < environment[1]:
            self.setPos(new_pos)  # updates position

        else:
            if new_pos[0] <= 0 or new_pos[0] >= environment[0]:
                self.direction = np.pi - self.direction
                delta_x = self.speed * t * np.cos(self.direction)
                new_pos = self.pos + np.asarray([delta_x, 0])

            if new_pos[1] <= 0 or new_pos[1] >= environment[1]-1:
                self.direction = -self.direction
                delta_y = self.speed * t * np.sin(self.direction)
                new_pos = self.pos + np.asarray([0, delta_y])

            self.setPos(new_pos)

        energy_loss = t * self.speed * self.speed  # energy loss proportional to t*v^2
        self.energy -= energy_loss
        print(self.pos)

    def eat(self):
        """eat food and reset energy"""
        self.energy = 100
