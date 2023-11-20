"""Environment Module

Classes:
    Environment

Functions:
    None
    
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
from CONSTANTS import *
from agent import Agent
from food import Food
import os
import pandas as pd
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Environment:
    """Environment Class
    
    Attributes:
        size (int): size of environment walls in m
        num_agents (int): number of agents in the environment
        num_food (int): number of food objects in the environment
        step_count (int): number of steps elapsed
        agent_list (list): list of agent objects
        food_list (list): list of food objects
        agent_data (list): list of agent data
        food_data (list): list of food data
        pop_data (list): list of population data
        food_spawn_rate (float): spawn rate of food
        mutation_count (int): number of mutations
        sim_name (string): simulation name for data saving

    """

    def __init__(self, sim_name=None):
        """Initialise environment

        """

        self.step_count = 0
        self.num_agents = 0
        self.num_food = 0
        self.sim_name = sim_name
        self.agent_list = []
        self.food_list = []
        self.food_data = []
        self.agent_data = []
        self.pop_data = []
        self.mutation_count = 0
        self.food_spawn_rate = FOOD_SPAWN_RATE
        self.size = ENV_SIZE
        self.animation = None
        self.mutation_rate = PROB_MUTATE
        self.mutation_size = 5

    def set_size(self, size):
        """Set environment size"""
        self.size = size

    @staticmethod
    def ring_coordinates():
        """Generate coordinates within a ring"""

        theta = random.uniform(0, 2*np.pi)
        r_squared = random.uniform(2500**2, 3000**2)
        r = np.sqrt(r_squared)
        x = r*np.cos(theta) + 4000
        y = r*np.sin(theta) + 4000
        return x, y

    def gen_pos_food(self):
        """Return a random position within environment"""

        # x = np.random.uniform(0, self.size)
        # y = np.random.uniform(0, self.size)

        p = random.random()

        if p < 0.5:
            r, theta = [np.sqrt(random.randint(0, 1000)) * np.sqrt(1000), 2 * np.pi * random.random()]
            x = 4000 + r * np.cos(theta)
            y = 4000 + r * np.sin(theta)

        else:
            x, y = self.ring_coordinates()

        return np.asarray([x, y])

    def set_food_spawn_rate(self, spawn_rate):
        self.food_spawn_rate = spawn_rate

    def gen_pos(self):
        """Return a random position within environment"""

        x = np.random.uniform(0, self.size)
        y = np.random.uniform(0, self.size)
        return np.asarray([x, y])

    def add_agent(self, init_pos=None, init_speed=None, init_size=None, init_energy=None):
        """Add agent into environment"""

        if init_pos is None:
            init_pos = self.gen_pos()

        agent = Agent(init_pos, init_speed, init_size, init_energy)
        self.agent_list.append(agent)
        self.num_agents += 1

        if self.animation:
            self.axes.add_patch(Agent.get_patch(agent))

    def get_agent(self):
        """Return agent with a given id"""
        for agent in self.agent_list:
            if Agent.get_id(agent) == id:
                return agent

    def add_food(self, init_pos=None):
        """Add food into environment"""
        if init_pos is None:
            init_pos = self.gen_pos_food()

        food = Food(init_pos)

        self.food_list.append(food)
        self.num_food += 1

        if self.animation:
            self.axes.add_patch(Food.get_patch())

    def importdata(self, data_file_path):
        """Import all csv files, unpack into dataframes, and return dictionary"""

        csv_files = [f for f in os.listdir(data_file_path) if f.endswith('.csv')]
        dataframes = {}

        for csv_file in csv_files:
            file_path = os.path.join(data_file_path, csv_file)
            dataframes[csv_file.split('.')[0]] = pd.read_csv(file_path)

        return dataframes

    def populate(self, init_agents, init_food):
        """Populate the environment with agents and food"""

        if CONTINUATION:
            dataframes = self.importdata()
            agents = dataframes['Agent_Data_mutation_1']
            food = dataframes['Food_Data_mutation_1']
            last_time = agents['Time Elapsed/s'].iloc[-1]

            agents = agents[agents['Time Elapsed/s'] == last_time]
            food = food[food['Time Elapsed'] == last_time]

            for i in range(len(agents)):
                position = (agents['X-Coord'].iloc[i], agents['Y-Coord'].iloc[i])
                self.add_agent(init_pos=position, init_size=agents['Size'].iloc[i], init_speed=agents['Speed'].iloc[i],
                               init_energy=agents['Energy'].iloc[i])

            for i in range(len(food)):
                position = (food['X-Coord'].iloc[i], food['Y-Coord'].iloc[i])
                self.add_food(init_pos=position)

        else:
            for i in range(0, init_agents):
                self.add_agent()
                self.num_agents += 1
            for i in range(0, init_food):
                self.add_food()
                self.num_food += 1

    def eat_check(self, agent):
        """Check for food nearby agent and eat"""

        del_list_food = []
        for food in self.food_list:
            if np.linalg.norm(agent.get_pos() - food.get_pos()) < (agent.get_size() + food.get_size()):
                food.remove_patch()
                del_list_food.append(food)
                self.num_food -= 1
                agent.eat_food(food)

        self.food_list = [food for food in self.food_list if food not in del_list_food]

    def check_point(self, agent):
        """Check for food within the agent's circle sector of vision"""

        points = []
        percentage = (agent.get_radius() ** 2 * agent.get_angle()) * 100 / (np.pi * agent.get_radius() ** 2)
        end = (2 * np.pi / percentage) + agent.get_angle()

        for food in self.food_list:
            position = food.get_pos()
            x = position[0]
            y = position[1]
            radius_f = np.sqrt(x ** 2 + y ** 2)
            angle_f = np.arctan(y / x)  # cartesian to polar

            if (angle_f >= agent.get_angle()) and (angle_f <= end) and (radius_f <= agent.get_radius()):
                points.append(food)

        return points

    def check_intercept(self, agent, points):
        """Check if points within an agent's sector of vision intercept the agent's rays"""

        eat_me = []  # change this at some point
        rays = agent.get_rays()

        for food in points:  # could combine this and check_point, make check_intercept a static method
            centre = food.get_pos()
            radius = food.get_size()

            for ray in rays:
                a, b, c = ray.get_equation_of_ray_line  # can be included in agent.get_rays() ?
                dist = (a * centre[0] + b * centre[1] + c) / np.sqrt(
                    a ** 2 + b ** 2)  # distance from ray to food centre
                if dist <= radius:
                    eat_me.append(food)

        return eat_me

    def divide(self, parent):
        """Duplicate agent"""

        child_pos = parent.get_pos() + np.asarray([0.01, 0.01])
        new_energy = parent.energy - INIT_ENERGY
        parent.set_energy(new_energy)

        speed, size = self.mutate(parent)
        self.add_agent(init_pos=child_pos, init_speed=speed, init_size=size)

    def mutate(self, parent: Agent):
        """Mutate and return new parameters"""

        speed = parent.get_speed()
        size = parent.get_size()

        if np.random.random() < self.mutation_rate:  # speed mutation
            self.mutation_count += 1
            mutation = np.random.poisson(self.mutation_size, None)
            while mutation == 0:
                mutation = np.random.poisson(self.mutation_size, None)

            speed = parent.get_speed() + (mutation * np.random.choice([-1, 1]))
            if speed < 0:
                speed = 0

        if np.random.random() < self.mutation_rate:  # size mutation
            self.mutation_count += 1
            mutation = np.random.poisson(self.mutation_size, None)
            while mutation == 0:
                mutation = np.random.poisson(self.mutation_size, None)

            size = parent.get_size() + (mutation * np.random.choice([-1, 1]))
            if size < 0:
                size = 0

        return speed, size

    def step(self):
        """Step a set time through the environment"""

        if self.num_agents == 0:
            raise Exception("No agents remaining")

        del_list_agent = []
        for agent in self.agent_list:
            agent.move()
            self.eat_check(agent)

            if agent.get_energy() < 0:
                agent.remove_patch()
                del_list_agent.append(agent)
                self.num_agents -= 1

            if agent.get_energy() > (REP_THRESHOLD * MAX_ENERGY):
                self.divide(parent=agent)

        self.agent_list = [agent for agent in self.agent_list if agent not in del_list_agent]

        if not self.food_spawn_rate == 0:
            if self.step_count % np.reciprocal(self.food_spawn_rate) == 0:
                self.add_food()

        self.step_count += 1

    def animate(self, i):
        """Animate environment using matplotlib"""

        self.step()
        self.step_text.set_text('Steps: ' + str(self.step_count))
        self.pop_text.set_text('Population: ' + str(self.num_agents))

        for agent in self.agent_list:
            agent.update_patch()

        for food in self.food_list:
            food.update_patch()

    def run(self, num_steps, animate=False, take_data=True):
        """Run simulation for num_steps"""

        if animate:
            self.fig = plt.figure(figsize=(6, 6))
            self.axes = plt.axes(xlim=(0, self.size), ylim=(0, self.size))
            self.step_text = self.axes.text(0.4 * self.size, 1.02 * self.size, '')
            self.pop_text = self.axes.text(0.6 * self.size, 1.02 * self.size, '')
            self.fig_title = self.axes.text(0.35 * self.size, 1.05 * self.size, 'Environment')

            for agent in self.agent_list:
                self.axes.add_patch(agent.patch)
            for food in self.food_list:
                self.axes.add_patch(food.patch)

            anim = animation.FuncAnimation(self.fig, self.animate, frames=num_steps, repeat=False,
                                           interval=10)

            plt.show()

        for i in range(num_steps):
            print(i)
            if self.num_agents == 0:
                raise Exception("First populate environment")

            self.step()

            if take_data:
                if self.step_count % DATA_INTERVAL != 0:
                    self.record_state()

        print("Run complete")

    def record_agents(self):
        """Append data for each agent instance to agent_data"""

        for agent in self.agent_list:
            pos = agent.get_pos()
            energy = agent.get_energy()
            ag_id = agent.get_id()
            speed = agent.get_speed()
            size = agent.get_size()

            energy_rounded = np.round(energy, 3)
            x_rounded = np.round(pos[0], 3)
            y_rounded = np.round(pos[1], 3)

            self.agent_data.append([self.step_count, ag_id, x_rounded, y_rounded, energy_rounded, speed, size])

    def record_pop(self):
        """Append population data to pop_data"""
        self.pop_data.append([self.step_count, self.num_agents, self.num_food])

    def record_food(self):
        """Append data for each food instance to food_data"""

        for food in self.food_list:
            pos = food.get_pos()
            f_id = food.get_id()

            x_rounded = np.round(pos[0], 3)
            y_rounded = np.round(pos[1], 3)

            self.food_data.append([self.step_count, f_id, x_rounded, y_rounded])

    def record_state(self):
        """Record all information about state"""
        self.record_agents()
        self.record_food()
        self.record_pop()

    def save_data(self, data_file_path):
        """Package all data into dataframe and save csvs to /data"""

        agent_df = pd.DataFrame(data=self.agent_data,
                                columns=['Time Elapsed/s', 'ID', 'X-Coord', 'Y-Coord', 'Energy', 'Speed', 'Size'])
        pop_df = pd.DataFrame(data=self.pop_data,
                              columns=['Time Elapsed/s', 'Agent Population', 'Food Population'])
        food_df = pd.DataFrame(data=self.food_data,
                               columns=['Time Elapsed', 'ID', 'X-Coord', 'Y-Coord'])

        agent_df.to_csv(f"{data_file_path}/agent_data_{self.sim_name}.csv",
                        index=False)

        pop_df.to_csv(f"{data_file_path}/pop_data_{self.sim_name}.csv",
                      index=False)

        food_df.to_csv(f"{data_file_path}/food_data_{self.sim_name}.csv",
                       index=False)
