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

def importdata(folder_path=r"C:\Users\alyss\OneDrive\Documents\GitHub\computational-evolution\computational-evolution"
                           r"\data"):
    """Import all csv files, unpack into dataframes, and return dictionary"""

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    dataframes = {}

    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        dataframes[csv_file.split('.')[0]] = pd.read_csv(file_path)

    return dataframes


dataframes = importdata()

# SIM 1

df_data1 = dataframes['Agent_Data_food_half_3']
# df_agent1 = df_data1[['Time Elapsed/s', 'Speed', 'Size']]
#
# df_agent1 = df_agent1.groupby(['Time Elapsed/s', 'Speed', 'Size']).size().reset_index(name='Count')
# df_agent1['Count'] = df_agent1['Count'] * 50
# df_speed1 = df_agent1.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size1 = df_agent1.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count1 = df_agent1.groupby(['Time Elapsed/s'])['Count'].apply(list)

# df_speed1 = df_speed1.iloc[::10] # Every 100 frames
# df_size1 = df_size1[::10]
# count1 = count1[::10]

df_pop1 = dataframes['Population_Data_food_half_3']

population1 = df_pop1['Agent Population']
food1 = df_pop1['Food Population']
times1 = df_pop1['Time Elapsed/s']
df_pop1['Mean Agent'] = df_pop1['Agent Population'].rolling(1000).mean()
df_pop1['Mean Food'] = df_pop1['Food Population'].rolling(1000).mean()

mean_ag = df_pop1['Mean Agent'].iloc[::1000]
mean_f = df_pop1['Mean Food'].iloc[::1000]
times = df_pop1['Time Elapsed/s'].iloc[::1000]


#

# pop1 = population1.iloc[2000]
# speed_ls1 = df_speed1.iloc[2000]
# size_ls1 = df_size1.iloc[2000]
# count1 = count1.iloc[2000]

# SIM 2
# df_data2 = dataframes['Agent_Data_mutation_2']
# df_agent2 = df_data2[['Time Elapsed/s', 'Speed', 'Size']]
#
# df_agent2 = df_agent2.groupby(['Time Elapsed/s', 'Speed', 'Size']).size().reset_index(name='Count')
# df_agent2['Count'] = df_agent2['Count'] * 50
# df_speed2 = df_agent2.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size2 = df_agent2.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count2 = df_agent2.groupby(['Time Elapsed/s'])['Count'].apply(list)
# #
# # df_speed2 = df_speed2.iloc[::10] # Every 100 frames
# # df_size2 = df_size2[::10]
# # count2 = count2[::10]
#
# df_pop2 = dataframes['Population_Data_mutation_2']
# df_pop2 = df_pop2[['Time Elapsed/s', 'Agent Population']]
#
# population2 = df_pop2['Agent Population']
# # population2 = population2[::10]
# pop2 = population2.iloc[-1]
# times2 = df_pop2['Time Elapsed/s']
# times2 = times2[::10]
# food_halve = df_agent.loc[19990]
# speed_ls2 = df_speed2.iloc[-1]
# size_ls2 = df_size2.iloc[-1]
# count2 = count2.iloc[-1]
#
# # SIM 3
# df_data3 = dataframes['Agent_Data_mutation_3']
# df_agent3 = df_data3[['Time Elapsed/s', 'Speed', 'Size']]
#
# df_agent3 = df_agent3.groupby(['Time Elapsed/s', 'Speed', 'Size']).size().reset_index(name='Count')
# df_agent3['Count'] = df_agent3['Count'] * 50
# df_speed3 = df_agent3.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size3 = df_agent3.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count3 = df_agent3.groupby(['Time Elapsed/s'])['Count'].apply(list)
#
# # df_speed3 = df_speed3.iloc[::10] # Every 300 frames
# # df_size1 = df_size3[::10]
# # count3 = count3[::10]
#
# df_pop3 = dataframes['Population_Data_mutation_3']
# df_pop3 = df_pop3[['Time Elapsed/s', 'Agent Population']]
#
# population3 = df_pop3['Agent Population']
# # population3 = population3[::10]
# pop3 = population3.iloc[-1]
# times3 = df_pop3['Time Elapsed/s']
# times3 = times3[::10]
#
# speed_ls3 = df_speed3.iloc[-1]
# size_ls3 = df_size3.iloc[-1]
# count3 = count3.iloc[-1]
#
# # SIM 4
# df_data4 = dataframes['Agent_Data_mutation_4']
# df_agent4 = df_data4[['Time Elapsed/s', 'Speed', 'Size']]
#
# df_agent4 = df_agent4.groupby(['Time Elapsed/s', 'Speed', 'Size']).size().reset_index(name='Count')
# df_agent4['Count'] = df_agent4['Count'] * 50
# df_speed4 = df_agent4.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size4 = df_agent4.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count4 = df_agent4.groupby(['Time Elapsed/s'])['Count'].apply(list)
#
# # df_speed4 = df_speed4.iloc[::10] # Every 100 frames
# # df_size4 = df_size4[::10]
# # count4 = count4[::10]
#
# df_pop4 = dataframes['Population_Data_mutation_4']
# df_pop4 = df_pop4[['Time Elapsed/s', 'Agent Population']]
#
# population4 = df_pop4['Agent Population']
# # population4 = population4[::10]
# pop4 = population4.iloc[-1]
# times4 = df_pop4['Time Elapsed/s']
# times4 = times4[::10]
#
# speed_ls4 = df_speed4.iloc[-1]
# size_ls4 = df_size4.iloc[-1]
# count4 = count4.iloc[-1]
#
# # SIM 5
# df_data5 = dataframes['Agent_Data_mutation_5']
# df_agent5 = df_data5[['Time Elapsed/s', 'Speed', 'Size']]
#
# df_agent5 = df_agent5.groupby(['Time Elapsed/s', 'Speed', 'Size']).size().reset_index(name='Count')
# df_agent5['Count'] = df_agent5['Count'] * 50
# df_speed5 = df_agent5.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size5 = df_agent5.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count5 = df_agent5.groupby(['Time Elapsed/s'])['Count'].apply(list)
#
# # df_speed5 = df_speed5.iloc[::10] # Every 100 frames
# # df_size5 = df_size5[::10]
# # count5 = count5[::10]
#
# df_pop5 = dataframes['Population_Data_mutation_5']
# df_pop5 = df_pop5[['Time Elapsed/s', 'Agent Population']]
#
# population5 = df_pop5['Agent Population']
# # population5 = population5[::10]
# pop5 = population5.iloc[-1]
# times5 = df_pop5['Time Elapsed/s']
# times5 = times5[::10]
#
# speed_ls5 = df_speed5.iloc[-1]
# size_ls5 = df_size5.iloc[-1]
# count5 = count5.iloc[-1]
#
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
# # plt.scatter(speed_ls2, size_ls2, color='green', s=count2, label=f'Population: {pop2}')
# # plt.scatter(speed_ls3, size_ls3, color='blue', s=count3, label=f'Population: {pop3}')
# # plt.scatter(speed_ls4, size_ls4, color='purple', s=count4, label=f'Population: {pop4}')
# # plt.scatter(speed_ls5, size_ls5, color='red', s=count5, label=f'Population: {pop5}')
#
# # plt.plot(low_speed_ls, high_size_ls, 'o', color='pink')
# # plt.plot(high_speed_ls, low_size_ls, 'o', color='black')
#
# plt.legend()
# #plt.show()
# plt.savefig('Speed vs Size Food Halve')

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

        self.step_text1 = self.ax.text(0.4 * 200, 1.01 * 200, '')
        self.pop_text1 = self.ax.text(0.7 * 200, 1.01 * 200, '')
        self.fig_title = self.ax.text(0.35 * 200, 1.05 * 200, 'Genespace')

        self.ax.scatter(df_speed1.iloc[i], df_size1.iloc[i], s=count1.iloc[i])
        self.step_text1.set_text('Steps: ' + str(times1.iloc[i]))
        self.pop_text1.set_text('Population: ' + str(population1.iloc[i]))

    def animate(self):
        anim = animation.FuncAnimation(self.fig, self.update, frames=len(times1), interval=0.1, repeat=False)

        plt.show()


# an = Animation()
# an.animate()

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

# df_agent = dataframes['Agent_Data_food_dist_1']
# df_agent = df_agent[5000:]
# df_agent = df_agent.groupby(['Time Elapsed/s', 'X-Coord', 'Y-Coord']).size().reset_index(name='Count')
# df_agent['Count'] = df_agent['Count'] * 50
# df_x = df_agent.groupby(['Time Elapsed/s'])['X-Coord'].apply(list)
# df_x = df_x[::100]
# df_y = df_agent.groupby(['Time Elapsed/s'])['Y-Coord'].apply(list)
# df_y = df_y[::100]
# count = df_agent.groupby(['Time Elapsed/s'])['Count'].apply(list)
# count = count[::100]

# df_agent = df_agent[5000:]
# df_agent = df_agent[::1000]
# df_pop = dataframes['Population_Data_upper_right_1']
# df_food = dataframes['Food_Data_upper_right_1']
# df_food = df_food[5000:]

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
plt.title('Agent and Food Population')
plt.xlabel('Frames Elapsed')
plt.ylabel('Population')
plt.grid()

plt.plot(times1, food1, color='blue', label='Food')
plt.plot(times1, population1, color='purple', label='Agents')
plt.plot(times, mean_ag, color='pink', label='Mean Agents')
plt.plot(times, mean_f, color='green', label='Mean Food')
plt.legend()

plt.savefig('Food Vs Agents')