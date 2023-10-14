from agent import Agent
from food import Food
from environment import Environment
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np


class Simulation:
    def __init__(self, num_agents, num_food):
        """allows steps through a simulation, with methods for extracting data

        Arguments:

        num_agents = number of agents to start the simulation

        num_food = number of food objects initially
        """

        self.num_agents = num_agents
        self.num_food = num_food
        self.agent_list = []
        self.food_list = []

        self.env = Environment(20, 3)  # possibly Simulation should allow env_size and agent_speed??

        for i in range(0, self.num_agents):  # populating environment
            self.agent_list.append(self.env.addAgent())

        for i in range(0, self.num_food):
            self.food_list.append(self.env.addFood())

    def step(self):
        # progress state forward by one step
        self.del_list_agents = []

        for i in range(0, self.num_agents):
            Agent.move(self.agent_list[i], 0.05)  # first move each agent in list

            if Agent.pos(self.agent_list[i])[
                0] > self.env.size:  # not allowing out of bounds - should test cons. energy
                Agent.setPos(self.agent_list[i], [self.env.size, Agent.pos(self.agent_list[i])[1]])

            if Agent.pos(self.agent_list[i])[0] < 0:
                Agent.setPos(self.agent_list[i], [0, Agent.pos(self.agent_list[i])[1]])

            if Agent.pos(self.agent_list[i])[1] > self.env.size:
                Agent.setPos(self.agent_list[i], [Agent.pos(self.agent_list[i])[0], self.env.size])

            if Agent.pos(self.agent_list[i])[1] < 0:
                Agent.setPos(self.agent_list[i], [Agent.pos(self.agent_list[i])[0], 0])

            if Agent.energy(self.agent_list[i]) <= 0:  # delete if no energy
                self.del_list_agents.append(self.agent_list[i])
                self.agent_patches[i].remove()  # removes corresponding agent patch

            del_list_food = []

            for j in range(0, self.num_food):  # next loop through to check for food within 1m

                if np.linalg.norm(np.subtract(Agent.pos(self.agent_list[i]), Food.pos(self.food_list[j]))) < 1:
                    Agent.eat(self.agent_list[i])
                    del_list_food.append(self.food_list[j]) # appending food objects to delete
                    self.food_patches[i].remove()

            self.food_list = [e for e in self.food_list if e not in del_list_food]
            self.num_food -= len(del_list_food)

        self.agent_list = [e for e in self.agent_list if e not in self.del_list_agents]
        self.num_agents -= len(self.del_list_agents)

    def animate(self, frame):
        """matplotlib animation function

        updates position of agents using self.step() and then updates and returns agent patches
        """
        self.step()
        #print(frame)

        for i in range(self.num_agents):
            self.agent_patches[i].center = Agent.pos(self.agent_list[i])

        for i in range(self.num_agents):
            self.agent_patches[i].center = Agent.pos(self.agent_list[i])

        return self.agent_patches, self.food_patches

    def run(self, num_steps: int, anim=True):
        """steps through num_steps using step method"""
        # could add additional arguments for data extraction (utilise other methods)

        if anim == True:  # use animate methods for step
            fig = plt.figure('Environment', figsize=(8, 8))

            axes = plt.axes(xlim=(0, self.env.size), ylim=(0, self.env.size))

            self.agent_patches = [patches.Circle(Agent.pos(agent), 1, fc='g') for agent in
                                  self.agent_list]  # initialise patches
            self.food_patches = [patches.Circle(Food.pos(food), 0.5, fc='r') for food in self.food_list]

            for i in self.agent_patches:  # add agent patches
                axes.add_patch(i)

            for i in self.food_patches:  # add food patches
                axes.add_patch(i)

            anim = animation.FuncAnimation(fig, self.animate, frames=num_steps, interval=10)

            plt.show()

        else:  # without animation
            for i in range(0, num_steps):
                self.step()


sim = Simulation(10, 10)

sim.run(10000, anim=True)
