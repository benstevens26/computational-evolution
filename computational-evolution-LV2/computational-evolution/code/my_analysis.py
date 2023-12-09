import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import matplotlib.animation as animation
import analysis
from CONSTANTS import *

file_path = r"C:\Users\alyss\OneDrive\Documents\Year 3 Physics\Project Data\data"

dataframes = analysis.import_data(file_path)


def get_energy_loss(speed, size):
    """Return energy loss per step"""
    t = TIME_STEP
    energy_loss = ((t * speed * speed) / 10000) * size + BASE_LOSS
    return energy_loss


df_data1 = dataframes['Agent_Data_food_half_3']
df_agent1 = df_data1[['Time Elapsed/s', 'Speed', 'Size']]
#
df_data2 = df_agent1.groupby(['Time Elapsed/s', 'Speed', 'Size']).size().reset_index(name='Count')
# df_agent1['Count'] = df_agent1['Count'] * 50
df_speed = df_agent1.groupby(['Time Elapsed/s'])['Speed'].mean().reset_index(name='Speed Mean')
df_size1 = df_agent1.groupby(['Time Elapsed/s'])['Size'].mean().reset_index(name='Size Mean')
df_mean = df_size1.merge(df_speed)
df_mean['Energy Loss'] = get_energy_loss(df_mean['Speed Mean'], df_mean['Size Mean'])

# count1 = df_agent1.groupby(['Time Elapsed/s'])['Count'].apply(list)

# df_speed1 = df_speed1.iloc[::10] # Every 100 frames
# df_size1 = df_size1[::10]
# count1 = count1[::10]

df_pop1 = dataframes['Population_Data_food_half_3']

# population1 = df_pop1['Agent Population']
# food1 = df_pop1['Food Population']
times = df_pop1['Time Elapsed/s']
# df_pop1['Mean Agent'] = df_pop1['Agent Population'].rolling(1000).mean()
# df_pop1['Mean Food'] = df_pop1['Food Population'].rolling(1000).mean()
#
# mean_ag = df_pop1['Mean Agent'].iloc[::1000]
# mean_f = df_pop1['Mean Food'].iloc[::1000]
# times = df_pop1['Time Elapsed/s'].iloc[::1000]

# pop1 = population1.iloc[2000]
# speed_ls1 = df_speed1.iloc[2000]
# size_ls1 = df_size1.iloc[2000]
# count1 = count1.iloc[2000]


# speed_ls = df_speed.iloc[-1]
# size_ls = df_size.iloc[-1]
# count = count.iloc[-1]
# #
# high_speed_ls = [i for i in speed_ls if i > 49]
# high_size_ls = [i for i in size_ls if i > 100]
# low_speed_ls = [i for i in speed_ls if i < 50]
# low_size_ls = [i for i in size_ls if i < 100]
#
# plt.figure()
# plt.grid()
# plt.title('Genespace at 20000th Step')
# plt.xlabel('Speed')
# plt.ylabel('Size')

# plt.scatter(speed_ls1, size_ls1, color='pink', s=count1, label=f'Population: {pop1}')

# # plt.plot(low_speed_ls, high_size_ls, 'o', color='pink')
# # plt.plot(high_speed_ls, low_size_ls, 'o', color='black')
#
# plt.legend()
# #plt.show()
# plt.savefig('Speed vs Size Food Halve')

# df_agent = df_data1.groupby(['Time Elapsed/s'], as_index=False).mean()
# x = df_agent['Time Elapsed/s']
# y = df_agent['Speed']
# #z = df_agent['Energy']
#
# df_pop = dataframes['Population_Data_food_half_2']
#
# df_pop = df_pop[['Time Elapsed/s', 'Agent Population']]
# y_pop = df_pop['Agent Population']
# #
# fig, ax = plt.subplots()
# plt.grid()
# ax.plot(x, y, color='green', label='Mean Speed')
# ax.set_xlabel('Time Elapsed (s)')
# ax.set_ylabel('Mean Speed')
# # ax1 = ax.twinx()
# # ax1.plot(x, y_pop, color='red', label='Agent Population')
# # ax1.set_ylabel('Agent Population')
# ax.legend(loc=0)
# #ax1.legend(loc=2)
# plt.savefig('Mean Speed')

# SPEED HISTOGRAM
# df_agent = df_data1.groupby(['Time Elapsed/s'])['Speed'].apply(list)
#
# food_halve = df_agent.loc[19990]
# df_last_step = df_agent.iloc[-1]
#
# plt.figure()
# plt.title('Speeds of Agents at Last Time Step')
# plt.xlabel('Speed')
# plt.ylabel('Number of Agents')
# plt.hist(df_last_step, bins=10, align='mid', color='purple', edgecolor='black')
# plt.savefig('Agent_Speed_Last_1')

# SPATIAL DISTRIBUTION OF AGENTS
# df_agent = df_data1[5000:]
# df_agent = df_agent.groupby(['Time Elapsed/s', 'X-Coord', 'Y-Coord']).size().reset_index(name='Count')
# df_agent['Count'] = df_agent['Count'] * 50
# df_x = df_agent.groupby(['Time Elapsed/s'])['X-Coord'].apply(list)
# df_x = df_x[::100]
# df_y = df_agent.groupby(['Time Elapsed/s'])['Y-Coord'].apply(list)
# df_y = df_y[::100]
# count = df_agent.groupby(['Time Elapsed/s'])['Count'].apply(list)
# count = count[::100]

# plt.title('Spatial Distribution of Agents')
# plt.xlabel('X-Coord')
# plt.ylabel('Y-Coord')
# plt.grid()
#
# for i in range(len(df_x)):
#     plt.scatter(df_x.iloc[i], df_y.iloc[i], s=count.iloc[i])
#
# plt.savefig('Food Dist')

# FOOD AND AGENT POPULATION
plt.figure()
plt.title('Change in Energy Loss')
plt.xlabel('Frames Elapsed')
plt.ylabel('Energy Loss')
plt.grid()
#
plt.plot(times, df_mean['Energy Loss'], color='blue', label='Food')

# plt.plot(times1, population1, color='purple', label='Agents')
# plt.plot(times, mean_ag, color='pink', label='Mean Agents')
# plt.plot(times, mean_f, color='green', label='Mean Food')
# plt.legend()
#
plt.savefig('Energy Loss')
