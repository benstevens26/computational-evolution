"""Analysis Module"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df_agent = pd.read_csv('computational-evolution/Data/Agent_Data_90612.csv')
df_food = pd.read_csv('computational-evolution/Data/Food_Data_90612.csv')
df_agent = pd.read_csv('computational-evolution/Data/Population_Data_90612.csv')

print(df_food)



y1 = df_agent['Agent Population']
y2 = df_agent['Food Population']
x = df_agent['Time Elapsed/s']

plt.figure()

plt.plot(x, y1, 'gx', label='Agent Population')
plt.plot(x, y2, 'rx', label='Food Population')


plt.legend()
plt.show()