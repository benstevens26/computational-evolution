"""Testing module"""

from environment import Environment
from time import time

data_path = r"C:\Users\alyss\OneDrive\Documents\Year 3 Physics\Project Data\data"
sims = 5

for i in range(sims):
    env = Environment(sim_name=i)
    env.populate(init_agents=40, init_food=40)
    env.run(num_steps=75000, animate=True)
    env.save_data(data_path)


