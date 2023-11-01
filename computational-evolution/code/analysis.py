"""Analysis Module

Classes:
    None

Functions:
    importData(): Import all csv files, unpack into datafrmes, and return dictionary

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


# import all data from folder

def importData(folder_path='C:/Users/alyss/OneDrive/Documents/GitHub/computational-evolution/computational-evolution'
                           '/data'):
    """Import all csv files, unpack into dataframes, and return dictionary"""

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    dataframes = {}

    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        dataframes[csv_file.split('.')[0]] = pd.read_csv(file_path)

    return dataframes


dataframes = importData()

# df_pop_20 = [df for df in dataframes if df.startswith('Population')]

df_agent = dataframes['Agent_Data_base_rate_4']

df_agent = df_agent[['Time Elapsed/s', 'Speed', 'Energy']]
df_agent = df_agent.groupby(['Time Elapsed/s'], as_index=False).mean()
x = df_agent['Time Elapsed/s']
y = df_agent['Speed']
#z = df_agent['Energy']

df_pop = dataframes['Population_Data_base_rate_4']

df_pop = df_pop[['Time Elapsed/s', 'Agent Population']]
y_pop = df_pop['Agent Population']
#
fig, ax = plt.subplots()
plt.grid()
ax.plot(x, y, color='green', label='Mean Speed')
plt.legend()
ax.set_xlabel('Time Elapsed (s)')
ax.set_ylabel('Mean Speed')
ax2 = ax.twinx()
ax2.plot(x, y_pop, color='red', label='Agent Population')
ax2.set_ylabel('Agent Population')
plt.legend()
plt.savefig('Mean_Speed_4')

# SPEED HISTOGRAM
# df_agent = df_agent.groupby(['Time Elapsed/s'])['Speed'].apply(list)
#
# df_last_step = df_agent.iloc[-1]
#
# plt.figure()
# plt.title('Speeds of Agents at Last Time Step')
# plt.xlabel('Speed')
# plt.ylabel('Number of Agents')
# plt.hist(df_last_step, bins=10, align='mid', color='purple', edgecolor='black')
# plt.savefig('Agent_Speed_Last_1')

# plt.grid()
# plt.plot(time, mean_s, color='green')
# plt.xlabel('Time Elapsed (s)')
# plt.ylabel('Mean Speed')
# plt.show()


# y1 = df_pop['Agent Population']
# y2 = df_pop['Food Population']
# x = df_pop['Time Elapsed/s']
#
# plt.figure()
#
# plt.plot(x, y1, 'go', markersize=1, label='Agent Population')
# plt.plot(x, y2, 'ro', markersize=1, label='Food Population')
#
#
# plt.legend()
# plt.show()
