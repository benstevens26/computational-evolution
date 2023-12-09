"""Testing module"""

from environment import Environment
from time import time
import numpy as np

# data_path = "/Users/benstevens/PycharmProjects/computational-evolution/computational-evolution/data"
data_path = r"C:\Users\alyss\OneDrive\Documents\Year 3 Physics\Project Data\data"

for i in [1, 2, 3]:
    env = Environment(sim_name=f'no_pred_{i}')
    env.populate(20, 15, 0)
    env.run(num_steps=35000, animate=False, take_data=True)
    env.save_data(data_path)
    print('Data Saved')

# for i in sims:
#     env = Environment(sim_name=f'evo_{i}')
#     env.populate(40, 30, 40)
#     env.run(num_steps=75000, animate=False, take_data=True)
#     env.save_data(data_path)

