"""Agent Module

Classes:
    Agent

Functions:
    None

"""

import numpy as np
import matplotlib.patches as patches
from CONSTANTS import *


class Agent:
    """Agent class
    
    Attributes:
        pos (array):
        speed (integer): Speed of agent
        size (integer): Size of agent
        energy (float): Energy of agent
        patch (matplotlib object): Graphical representation of agent
        direction (float): Direction of agent
    """

    def __init__(self, pos, speed=None, size=None, energy=None):
        """Initialise agent

        """

        if isinstance(pos, list):
            pos = np.asarray(pos)

        if speed is None:
            self.speed = np.random.randint(50, 150)
        else:
            self.speed = speed

        if size is None:
            self.size = np.random.randint(50, 150)
        else:
            self.size = size

        if energy is None:
            self.energy = INIT_ENERGY
        else:
            self.energy = energy

        # self.speed = 100
        # self.size = 100

        self.pos = pos  # assign position, energy, and direction
        self.direction = np.random.uniform(-np.pi, np.pi)
        self.patch = patches.Circle(self.pos, self.size, fc='blue')
        self.rep_threshold = REP_THRESHOLD
        self.correlation = 0.2
        self.angle = np.random.uniform(0, 3*np.pi/2)
        self.radius = (np.sqrt(MAX_SIGHT / self.angle) + self.size)
        self.vision_patch = patches.Wedge(self.pos, self.radius, theta1=(180/np.pi)*(self.direction-self.angle/2), theta2=(180/np.pi)*(self.direction+self.angle/2), alpha=0.3)


    def get_pos(self):
        """Return agent position"""
        return self.pos

    def set_pos(self, new_pos):
        """Set agent position"""
        if isinstance(new_pos, list):
            new_pos = np.asarray(new_pos)
        self.pos = new_pos

    def get_speed(self):
        """Return agent speed"""
        return self.speed

    def get_energy(self):
        """Return agent energy"""
        return self.energy

    def get_size(self):
        """Return agent size"""
        return self.size

    def get_radius(self):
        """Return radius of agent's sight"""
        return self.radius

    def get_angle(self):
        """Return the angle of the agent's sight"""
        return self.angle

    def set_energy(self, new_energy):
        """Set agent energy"""
        self.energy = new_energy

    def get_patch(self):
        """Return patch object"""
        return self.patch

    def get_direction(self):
        """Return agent direction"""
        return self.direction

    def eat_food(self, food):
        """Increase agent energy by energy of food"""
        eat_energy = food.energy
        new_energy = self.get_energy() + eat_energy
        self.set_energy(new_energy)

        if self.energy > MAX_ENERGY:
            self.set_energy(MAX_ENERGY)

    def get_energy_loss(self):
        """Return energy loss per step"""
        t = TIME_STEP
        energy_loss = ((t * self.speed * self.speed) / 10000) * self.size + BASE_LOSS
        return energy_loss

    def get_id(self):
        """Return agent UID"""
        return id(self)

    def rand_walk(self, t, direction=None):
        """Return dx, dy for a correlated random walk"""

        cone = np.pi / 4
        if direction is None:
            new_direction = self.direction + np.random.uniform(-cone, cone)
            self.set_correlation(c=0.2)

        else:
            new_direction = direction

        self.direction = self.correlation * new_direction + (1 - self.correlation) * self.direction

        delta_x = self.speed * t * np.cos(self.direction)
        delta_y = self.speed * t * np.sin(self.direction)

        new_pos = self.pos + np.asarray([delta_x, delta_y])

        if not 0 < new_pos[0] <= ENV_SIZE:  # this code should be environment - side
            new_pos[0] = new_pos[0] % ENV_SIZE
            delta_x = new_pos[0] - self.pos[0]

        if not 0 < new_pos[1] <= ENV_SIZE:
            new_pos[1] = new_pos[1] % ENV_SIZE
            delta_y = new_pos[1] - self.pos[1]

        return delta_x, delta_y

    def move(self, direction):
        """Move agent one step, update position, decrease energy"""

        t = TIME_STEP
        dx, dy = self.rand_walk(t, direction)  # generate dx, dy for random walk
        self.pos += np.asarray([dx, dy])

        new_energy = self.energy - self.get_energy_loss()
        self.set_energy(new_energy)

    def update_patch(self):
        """Update patch attribute centre"""
        self.patch.center = self.pos
        self.vision_patch.set_center(self.pos)
        self.vision_patch.set_theta1((180/np.pi) * (self.direction-self.angle/2))
        self.vision_patch.set_theta2((180/np.pi) * (self.direction+self.angle/2))

    def remove_patch(self):
        """Remove patch attribute"""
        self.patch.set_visible(False)
        self.vision_patch.set_visible(False)

    def set_direction(self, direction):
        """Change the direction of the agent"""
        self.direction = direction

    def set_correlation(self, c):
        """Change the correlation factor"""
        self.correlation = c
