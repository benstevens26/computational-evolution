"""Testing module"""

from environment import Environment
from time import time

data_path = "/Users/benstevens/PycharmProjects/computational-evolution/computational-evolution/data"
env = Environment('ben')
env.populate(20, 20, 10)

env.run(num_steps=10000, animate=True)
env.save_data(data_path)    
