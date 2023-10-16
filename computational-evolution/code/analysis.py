"""Analysis Module"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#df_agent = pd.read_csv('computational-evolution/Data/Agent_Data_58458.csv')
#df_food = pd.read_csv('computational-evolution/Data/Food_Data_58458.csv')
df_pop = pd.read_csv('computational-evolution/Data/Population_Data_6413.csv')


y1 = df_pop['Agent Population']
y2 = df_pop['Food Population']
x = df_pop['Time Elapsed/s']

plt.figure()

plt.plot(x, y1, 'go', markersize=1, label='Agent Population')
plt.plot(x, y2, 'ro', markersize=1, label='Food Population')


plt.legend()
plt.show()