"""Testing module"""

from environment import Environment
from time import time

# data_path = "/Users/benstevens/PycharmProjects/computational-evolution/computational-evolution/data"
data_path = r"C:\Users\alyss\OneDrive\Documents\Year 3 Physics\Project Data\data"
sims = 5

for i in range(sims):
    env = Environment(sim_name=i)
    env.populate(40, 40, 0)
    env.run(num_steps=75000, animate=False, take_data=True)
    env.save_data(data_path)
