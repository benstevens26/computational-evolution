"""Testing module"""

from environment import Environment
from time import time
from tqdm import tqdm

data_path_ben = "/Users/benstevens/PycharmProjects/computational-evolution-LV/computational-evolution/data"
# data_path = r"C:\Users\alyss\OneDrive\Documents\Year 3 Physics\Project Data\data"

sims = 0
total = 0
while sims < 6:
    total += 1
    env = Environment(sim_name=str(sims+1))
    env.populate(50, 0, 50)
    run = env.run(num_steps=25000, animate=False, take_data=True)
    if run == 1:
        env.save_data(data_path_ben)
        sims += 1

print("6 successful simulations completed")
print("Total simulation attempts =",total)



