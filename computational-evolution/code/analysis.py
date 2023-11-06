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
import matplotlib.animation as animation


# import all data from folder

def importData(folder_path="C:/Users/alyss/OneDrive/Documents/Year 3 Physics/Project Data/data"):
    """Import all csv files, unpack into dataframes, and return dictionary"""

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    dataframes = {}

    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        dataframes[csv_file.split('.')[0]] = pd.read_csv(file_path)

    return dataframes


dataframes = importData()

df_data = dataframes['Agent_Data_size_1']
df_agent = df_data[['Time Elapsed/s', 'Speed', 'Size']]

df_agent = df_agent.groupby(['Time Elapsed/s', 'Speed', 'Size']).size().reset_index(name='Count')
df_agent['Count'] = df_agent['Count']*50
df_speed = df_agent.groupby(['Time Elapsed/s'])['Speed'].apply(list)
df_size = df_agent.groupby(['Time Elapsed/s'])['Size'].apply(list)
count = df_agent.groupby(['Time Elapsed/s'])['Count'].apply(list)

df_pop = dataframes['Population_Data_size_1']
df_pop = df_pop[['Time Elapsed/s', 'Agent Population']]

population = df_pop['Agent Population']
times = df_pop['Time Elapsed/s']


class Animation:

    def __init__(self):
        self.fig = plt.figure('Genespace', figsize=(6, 6))
        self.ax = plt.axes(xlim=(0, 200), ylim=(0, 200))

    def update(self, i):
        self.ax.clear()

        self.ax.set_xlim(0, 200)
        self.ax.set_ylim(0, 200)
        self.ax.set_xlabel('Speed')
        self.ax.set_ylabel('Size')

        self.step_text1 = self.ax.text(0.4 * 200, 1.02 * 200, '')
        self.pop_text1 = self.ax.text(0.7 * 200, 1.02 * 200, '')
        self.fig_title = self.ax.text(0.35 * 200, 1.05 * 200, 'Genespace')

        self.ax.scatter(df_speed.iloc[i], df_size.iloc[i], s=count.iloc[i])
        self.step_text1.set_text('Steps: ' + str(times.iloc[i]))
        self.pop_text1.set_text('Population: ' + str(population.iloc[i]))

    def animate(self):
        anim = animation.FuncAnimation(self.fig, self.update, frames=len(times), interval=0.1, repeat=False)

        plt.show()


an = Animation()

an.animate()

# df_agent = df_agent.groupby(['Time Elapsed/s'], as_index=False).mean()
# x = df_agent['Time Elapsed/s']
# y = df_agent['Speed']
# #z = df_agent['Energy']
#
# df_pop = dataframes['Population_Data_base_rate_4']
#
# df_pop = df_pop[['Time Elapsed/s', 'Agent Population']]
# y_pop = df_pop['Agent Population']
# #
# fig, ax = plt.subplots()
# plt.grid()
# ax.plot(x, y, color='green', label='Mean Speed')
# plt.legend()
# ax.set_xlabel('Time Elapsed (s)')
# ax.set_ylabel('Mean Speed')
# ax2 = ax.twinx()
# ax2.plot(x, y_pop, color='red', label='Agent Population')
# ax2.set_ylabel('Agent Population')
# plt.legend()
# plt.show()

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
