"""Testing module"""

from environment import Environment
import pandas as pd

pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 1000)

env = Environment()

env.run()