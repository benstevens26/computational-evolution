import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import matplotlib.animation as animation
from CONSTANTS import *

def get_energy_loss(speed, size):
    """Return energy loss per step"""
    t = TIME_STEP
    energy_loss = ((t * speed * speed) / 10000) * size + BASE_LOSS
    return energy_loss


df_data1 = pd.read_pickle('d1.pkl')
df_pop1 = pd.read_pickle('p1.pkl')
df_pred1 = pd.read_pickle('pr1.pkl')

df_agent1 = df_data1[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
df_agent1 = df_agent1.tail(15000)
# #
df_agent1 = df_agent1.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
df_agent1['Count'] = df_agent1['Count'] * 50
df_speed1 = df_agent1.groupby(['Time Elapsed/s'])['Speed'].apply(list)
df_size1 = df_agent1.groupby(['Time Elapsed/s'])['Size'].apply(list)
df_angle1 = df_agent1.groupby(['Time Elapsed/s'])['Angle'].apply(list)
# x1 = df_agent1.groupby(['Time Elapsed/s'])['X-Coord'].apply(list)
# y1 = df_agent1.groupby(['Time Elapsed/s'])['Y-Coord'].apply(list)
# df_mean = df_size1.merge(df_speed)
# df_mean['Energy Loss'] = get_energy_loss(df_mean['Speed Mean'], df_mean['Size Mean'])

count1 = df_agent1.groupby(['Time Elapsed/s'])['Count'].apply(list)

# df_speed1 = df_speed1.iloc[::10]  # Every 100 frames
# df_size1 = df_size1[::10]
# count1 = count1[::10]

population1 = df_pop1['Agent Population']
times1 = df_pop1['Time Elapsed/s']
# df_pop1['Mean Agent'] = df_pop1['Agent Population'].rolling(1000).mean()
# df_pop1['Mean Food'] = df_pop1['Food Population'].rolling(1000).mean()
#
# mean_ag = df_pop1['Mean Agent'].iloc[::1000]
# mean_f = df_pop1['Mean Food'].iloc[::1000]
# times1 = df_pop1['Time Elapsed/s'].iloc[::10]
#
# pop1 = population1.iloc[::10]

speed1 = df_speed1.iloc[-1]
size1 = df_size1.iloc[-1]
count1 = count1.iloc[-1]
pop1 = population1.iloc[-1]
angle1 = df_angle1.iloc[-1]
# y1 = y1.iloc[-1]
# x1 = x1.iloc[-1]


df_pred1 = df_pred1[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
df_pred1 = df_pred1.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')

df_pred1['Count'] = df_pred1['Count'] * 50
df_speedp1 = df_pred1.groupby(['Time Elapsed/s'])['Speed'].apply(list)
df_sizep1 = df_pred1.groupby(['Time Elapsed/s'])['Size'].apply(list)
countp1 = df_pred1.groupby(['Time Elapsed/s'])['Count'].apply(list)
df_anglep1 = df_pred1.groupby(['Time Elapsed/s'])['Angle'].apply(list)

speedp1 = df_speedp1.iloc[-1]
sizep1 = df_sizep1.iloc[-1]
countp1 = countp1.iloc[-1]
anglep1 = df_anglep1.iloc[-1]
popp1 = len(speedp1)

# SECOND RUN
df_data2 = pd.read_pickle('d2.pkl')
df_pop2 = pd.read_pickle('p2.pkl')
df_pred2 = pd.read_pickle('pr2.pkl')

df_agent2 = df_data2[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
df_agent2 = df_agent2.tail(15000)

df_agent2 = df_agent2.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
df_agent2['Count'] = df_agent2['Count'] * 50
df_speed2 = df_agent2.groupby(['Time Elapsed/s'])['Speed'].apply(list)
df_size2 = df_agent2.groupby(['Time Elapsed/s'])['Size'].apply(list)
count2 = df_agent2.groupby(['Time Elapsed/s'])['Count'].apply(list)
df_angle2 = df_agent2.groupby(['Time Elapsed/s'])['Angle'].apply(list)
# x2 = df_agent2.groupby(['Time Elapsed/s'])['X-Coord'].apply(list)
# y2 = df_agent2.groupby(['Time Elapsed/s'])['Y-Coord'].apply(list)


population2 = df_pop2['Agent Population']
times2 = df_pop2['Time Elapsed/s']
times2 = df_pop2['Time Elapsed/s'].iloc[::10]

speed2 = df_speed2.iloc[-1]
size2 = df_size2.iloc[-1]
count2 = count2.iloc[-1]
angle2 = df_angle2.iloc[-1]
pop2 = population2.iloc[-1]
# x2 = x2.iloc[-1]
# y2 = y2.iloc[-1]

df_pred2 = df_pred2[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
df_pred2 = df_pred2.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')

df_pred2['Count'] = df_pred2['Count'] * 50
df_speedp2 = df_pred2.groupby(['Time Elapsed/s'])['Speed'].apply(list)
df_sizep2 = df_pred2.groupby(['Time Elapsed/s'])['Size'].apply(list)
countp2 = df_pred2.groupby(['Time Elapsed/s'])['Count'].apply(list)
df_anglep2 = df_pred2.groupby(['Time Elapsed/s'])['Angle'].apply(list)

speedp2 = df_speedp2.iloc[-1]
sizep2 = df_sizep2.iloc[-1]
countp2 = countp2.iloc[-1]
anglep2 = df_anglep2.iloc[-1]
popp2 = len(speedp2)

# THIRD RUN
# df_data3 = pd.read_pickle('d3.pkl')
# df_pop3 = pd.read_pickle('p3.pkl')
# df_pred3 = pd.read_pickle('pr3.pkl')

# df_agent3 = df_data3[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_agent3 = df_agent3.tail(15000)
#
# df_agent3 = df_agent3.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_agent3['Count'] = df_agent3['Count'] * 50
# df_speed3 = df_agent3.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size3 = df_agent3.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count3 = df_agent3.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_angle3 = df_agent3.groupby(['Time Elapsed/s'])['Angle'].apply(list)
# x3 = df_agent3.groupby(['Time Elapsed/s'])['X-Coord'].apply(list)
# y3 = df_agent3.groupby(['Time Elapsed/s'])['Y-Coord'].apply(list)

# population3 = df_pop3['Agent Population']
# times3 = df_pop3['Time Elapsed/s']
#times3 = df_pop3['Time Elapsed/s'].iloc[::10]

# speed3 = df_speed3.iloc[-1]
# size3 = df_size3.iloc[-1]
# count3 = count3.iloc[-1]
#angle3 = df_angle3.iloc[-1]
# pop3 = population3.iloc[-1]
# x3 = x3.iloc[-1]
# y3 = y3.iloc[-1]

# df_pred3 = df_pred3[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# popp3 = len(df_pred3.iloc[-1])
# timep3 = df_pred3['Time Elapsed/s'].iloc[-1]
# df_pred3 = df_pred3.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')

# df_pred3['Count'] = df_pred3['Count'] * 50
# df_speedp3 = df_pred3.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_sizep3 = df_pred3.groupby(['Time Elapsed/s'])['Size'].apply(list)
# countp3 = df_pred3.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_anglep3 = df_pred3.groupby(['Time Elapsed/s'])['Angle'].apply(list)

# speedp3 = df_speedp3.iloc[-1]
# sizep3 = df_sizep3.iloc[-1]
# countp3 = countp3.iloc[-1]
# anglep3 = df_anglep3.iloc[-1]

# FOURTH RUN
# df_data4 = pd.read_pickle('d4.pkl')
# df_pop4 = pd.read_pickle('p4.pkl')
# df_pred4 = pd.read_pickle('pr4.pkl')

# df_agent4 = df_data4[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_agent4 = df_agent4.tail(15000)
#
# df_agent4 = df_agent4.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_agent4['Count'] = df_agent4['Count'] * 50
# df_speed4 = df_agent4.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size4 = df_agent4.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count4 = df_agent4.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_angle4 = df_agent4.groupby(['Time Elapsed/s'])['Angle'].apply(list)
# x4 = df_agent4.groupby(['Time Elapsed/s'])['X-Coord'].apply(list)
# y4 = df_agent4.groupby(['Time Elapsed/s'])['Y-Coord'].apply(list)


# population4 = df_pop4['Agent Population']
# times4 = df_pop4['Time Elapsed/s']
# times4 = df_pop4['Time Elapsed/s'].iloc[::10]

# speed4 = df_speed4.iloc[-1]
# size4 = df_size4.iloc[-1]
# count4 = count4.iloc[-1]
# pop4 = population4.iloc[-1]
#angle4 = df_angle4.iloc[-1]
# x4 = x4.iloc[-1]
# y4 = y4.iloc[-1]

# df_pred4 = df_pred4[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# popp4 = len(df_pred4.iloc[-1])
# timep4 = df_pred4['Time Elapsed/s'].iloc[-1]
# df_pred4 = df_pred4.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
#
# df_pred4['Count'] = df_pred4['Count'] * 50
# df_speedp4 = df_pred4.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_sizep4 = df_pred4.groupby(['Time Elapsed/s'])['Size'].apply(list)
# countp4 = df_pred4.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_anglep4 = df_pred4.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# speedp4 = df_speedp4.iloc[-1]
# sizep4 = df_sizep4.iloc[-1]
# countp4 = countp4.iloc[-1]
# anglep4 = df_anglep4.iloc[-1]

# FIFTH RUN
# df_data5 = pd.read_pickle('d5.pkl')
# df_pop5 = pd.read_pickle('p5.pkl')
# df_pred5 = pd.read_pickle('pr5.pkl')

# df_agent5 = df_data5[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_agent5 = df_agent5.tail(15000)
#
# df_agent5 = df_agent5.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_agent5['Count'] = df_agent5['Count'] * 50
# df_speed5 = df_agent5.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size5 = df_agent5.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count5 = df_agent5.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_angle5 = df_agent5.groupby(['Time Elapsed/s'])['Angle'].apply(list)
# x5 = df_agent5.groupby(['Time Elapsed/s'])['X-Coord'].apply(list)
# y5 = df_agent5.groupby(['Time Elapsed/s'])['Y-Coord'].apply(list)


# population5 = df_pop5['Agent Population']
# times5 = df_pop5['Time Elapsed/s']

# speed5 = df_speed5.iloc[-1]
# size5 = df_size5.iloc[-1]
# count5 = count5.iloc[-1]
# pop5 = population5.iloc[-1]
#angle5 = df_angle5.iloc[-1]
# x5 = x5.iloc[-1]
# y5 = y5.iloc[-1]

# df_pred5 = df_pred5[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# popp5 = len(df_pred5.iloc[-1])
# timep5 = df_pred5['Time Elapsed/s'].iloc[-1]
# df_pred5 = df_pred5.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
#
# df_pred5['Count'] = df_pred5['Count'] * 50
# df_speedp5 = df_pred5.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_sizep5 = df_pred5.groupby(['Time Elapsed/s'])['Size'].apply(list)
# countp5 = df_pred5.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_anglep5 = df_pred5.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# speedp5 = df_speedp5.iloc[-1]
# sizep5 = df_sizep5.iloc[-1]
# countp5 = countp5.iloc[-1]
# anglep5 = df_anglep5.iloc[-1]

# SIXTH RUN
df_data6 = pd.read_pickle('d6.pkl')
df_pop6 = pd.read_pickle('p6.pkl')
df_pred6 = pd.read_pickle('pr6.pkl')

df_agent6 = df_data6[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
df_agent6 = df_agent6.tail(15000)

df_agent6 = df_agent6.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
df_agent6['Count'] = df_agent6['Count'] * 50
df_speed6 = df_agent6.groupby(['Time Elapsed/s'])['Speed'].apply(list)
df_size6 = df_agent6.groupby(['Time Elapsed/s'])['Size'].apply(list)
count6 = df_agent6.groupby(['Time Elapsed/s'])['Count'].apply(list)
df_angle6 = df_agent6.groupby(['Time Elapsed/s'])['Angle'].apply(list)

population6 = df_pop6['Agent Population']
times6 = df_pop6['Time Elapsed/s']

speed6 = df_speed6.iloc[-1]
size6 = df_size6.iloc[-1]
count6 = count6.iloc[-1]
pop6 = population6.iloc[-1]
angle6 = df_angle6.iloc[-1]

df_pred6 = df_pred6[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
df_pred6 = df_pred6.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')

df_pred6['Count'] = df_pred6['Count'] * 50
df_speedp6 = df_pred6.groupby(['Time Elapsed/s'])['Speed'].apply(list)
df_sizep6 = df_pred6.groupby(['Time Elapsed/s'])['Size'].apply(list)
countp6 = df_pred6.groupby(['Time Elapsed/s'])['Count'].apply(list)
df_anglep6 = df_pred6.groupby(['Time Elapsed/s'])['Angle'].apply(list)

speedp6 = df_speedp6.iloc[-1]
sizep6 = df_sizep6.iloc[-1]
countp6 = countp6.iloc[-1]
anglep6 = df_anglep6.iloc[-1]
popp6 = len(speedp6)

# SEVENTH RUN
# df_data7 = pd.read_pickle('d7.pkl')
# df_pop7 = pd.read_pickle('p7.pkl')
# df_pred7 = pd.read_pickle('pr7.pkl')

# df_agent7 = df_data7[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_agent7 = df_agent7.tail(15000)
#
# df_agent7 = df_agent7.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_agent7['Count'] = df_agent7['Count'] * 50
# df_speed7 = df_agent7.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size7 = df_agent7.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count7 = df_agent7.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_angle7 = df_agent7.groupby(['Time Elapsed/s'])['Angle'].apply(list)


# population7 = df_pop7['Agent Population']
# times7 = df_pop7['Time Elapsed/s']

# speed7 = df_speed7.iloc[-1]
# size7 = df_size7.iloc[-1]
# count7 = count7.iloc[-1]
# pop7 = population6.iloc[-1]
#angle7 = df_angle7.iloc[-1]

# df_pred7 = df_pred7[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# popp7 = len(df_pred7.iloc[-1])
# timep7 = df_pred7['Time Elapsed/s'].iloc[-1]
# df_pred7 = df_pred7.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
#
# df_pred7['Count'] = df_pred7['Count'] * 50
# df_speedp7 = df_pred7.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_sizep7 = df_pred7.groupby(['Time Elapsed/s'])['Size'].apply(list)
# countp7 = df_pred7.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_anglep7 = df_pred7.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# speedp7 = df_speedp7.iloc[-1]
# sizep7 = df_sizep7.iloc[-1]
# countp7 = countp7.iloc[-1]
# anglep7 = df_anglep7.iloc[-1]

# EIGHTH RUN
df_data8 = pd.read_pickle('d8.pkl')
df_pop8 = pd.read_pickle('p8.pkl')
df_pred8 = pd.read_pickle('pr8.pkl')

df_agent8 = df_data8[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
df_agent8 = df_agent8.tail(15000)

df_agent8 = df_agent8.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
df_agent8['Count'] = df_agent8['Count'] * 50
df_speed8 = df_agent8.groupby(['Time Elapsed/s'])['Speed'].apply(list)
df_size8 = df_agent8.groupby(['Time Elapsed/s'])['Size'].apply(list)
count8 = df_agent8.groupby(['Time Elapsed/s'])['Count'].apply(list)
df_angle8 = df_agent8.groupby(['Time Elapsed/s'])['Angle'].apply(list)

population8 = df_pop8['Agent Population']
times8 = df_pop8['Time Elapsed/s']

speed8 = df_speed8.iloc[-1]
size8 = df_size8.iloc[-1]
count8 = count8.iloc[-1]
pop8 = population8.iloc[-1]
angle8 = df_angle8.iloc[-1]

df_pred8 = df_pred8[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
df_pred8 = df_pred8.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')

df_pred8['Count'] = df_pred8['Count'] * 50
df_speedp8 = df_pred8.groupby(['Time Elapsed/s'])['Speed'].apply(list)
df_sizep8 = df_pred8.groupby(['Time Elapsed/s'])['Size'].apply(list)
countp8 = df_pred8.groupby(['Time Elapsed/s'])['Count'].apply(list)
df_anglep8 = df_pred8.groupby(['Time Elapsed/s'])['Angle'].apply(list)

speedp8 = df_speedp8.iloc[-1]
sizep8 = df_sizep8.iloc[-1]
countp8 = countp8.iloc[-1]
anglep8 = df_anglep8.iloc[-1]
popp8 = len(speedp8)

# NINTH RUN
# df_data9 = pd.read_pickle('d9.pkl')
# df_pop9 = pd.read_pickle('p9.pkl')
# df_pred9 = pd.read_pickle('pr9.pkl')

# df_agent9 = df_data9[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_agent9 = df_agent9.tail(15000)
#
# df_agent9 = df_agent9.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_agent9['Count'] = df_agent9['Count'] * 50
# df_speed9 = df_agent9.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size9 = df_agent9.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count9 = df_agent9.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_angle9 = df_agent9.groupby(['Time Elapsed/s'])['Angle'].apply(list)

# population9 = df_pop9['Agent Population']
# times9 = df_pop9['Time Elapsed/s']

# speed9 = df_speed9.iloc[-1]
# size9 = df_size9.iloc[-1]
# count9 = count9.iloc[-1]
# pop9 = population9.iloc[-1]
#angle9 = df_angle9.iloc[-1]

# df_pred9 = df_pred9[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# popp9 = len(df_pred9.iloc[-1])
# timep9 = df_pred9['Time Elapsed/s'].iloc[-1]
# df_pred9 = df_pred9.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
#
# df_pred9['Count'] = df_pred9['Count'] * 50
# df_speedp9 = df_pred9.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_sizep9 = df_pred9.groupby(['Time Elapsed/s'])['Size'].apply(list)
# countp9 = df_pred9.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_anglep9 = df_pred9.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# speedp9 = df_speedp9.iloc[-1]
# sizep9 = df_sizep9.iloc[-1]
# countp9 = countp9.iloc[-1]
# anglep9 = df_anglep9.iloc[-1]

# TENTH RUN
# df_data10 = pd.read_pickle('d10.pkl')
# df_pop10 = pd.read_pickle('p10.pkl')
# df_pred10 = pd.read_pickle('pr10.pkl')

# df_agent10 = df_data10[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_agent10 = df_agent10.tail(15000)
#
# df_agent10 = df_agent10.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_agent10['Count'] = df_agent10['Count'] * 50
# df_speed10 = df_agent10.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size10 = df_agent10.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count10 = df_agent10.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_angle10 = df_agent10.groupby(['Time Elapsed/s'])['Angle'].apply(list)

# population10 = df_pop10['Agent Population']
# times10 = df_pop10['Time Elapsed/s']

# speed10 = df_speed10.iloc[-1]
# size10 = df_size10.iloc[-1]
# count10 = count10.iloc[-1]
# pop10 = population10.iloc[-1]
#angle10 = df_angle10.iloc[-1]

# df_pred10 = df_pred10[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# popp10 = len(df_pred10.iloc[-1])
# timep10 = df_pred10['Time Elapsed/s'].iloc[-1]
# df_pred10 = df_pred10.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
#
# df_pred10['Count'] = df_pred10['Count'] * 50
# df_speedp10 = df_pred10.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_sizep10 = df_pred10.groupby(['Time Elapsed/s'])['Size'].apply(list)
# countp10 = df_pred10.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_anglep10 = df_pred10.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# speedp10 = df_speedp10.iloc[-1]
# sizep10 = df_sizep10.iloc[-1]
# countp10 = countp10.iloc[-1]
# anglep10 = df_anglep10.iloc[-1]

# SCATTERPLOT - GENESPACE
# plt.grid()
# plt.xlim(0, 60)
# plt.ylim(0, 200)

# plt.title('Spatial Distribution')
# plt.xlabel('X Coordinate')
# plt.ylabel('Y Coordinate')
# #
# plt.scatter(x1, y1, color='red')
# plt.scatter(x2, y2, color='green')
# plt.scatter(x3, y3, color='pink')
# plt.scatter(x4, y4, color='purple')
# plt.scatter(x5, y5, color='orange')
# plt.scatter(speed1, size1, s=count1, color='red', label=f'Population:{pop1}')
# plt.scatter(speed2, size2, s=count2, color='green', label=f'Population:{pop2}')
# plt.scatter(speed3, size3, s=count3, color='pink', label=f'Population:{pop3}')
# plt.scatter(speed4, size4, s=count4, color='purple', label=f'Population:{pop4}')
# plt.scatter(speed5, size5, s=count5, color='orange', label=f'Population:{pop5}')
# plt.legend()
# plt.savefig('Spatial Distribution')
# plt.show()

# anim = analysis.Animation(times, df_speed1, pop1, count1, df_size1)
# anim.animate()

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
# plt.figure()
# plt.title('Change in Energy Loss')
# plt.xlabel('Frames Elapsed')
# plt.ylabel('Energy Loss')
# plt.grid()
#
# plt.plot(times, df_mean['Energy Loss'], color='blue', label='Food')

# plt.plot(times1, population1, color='purple', label='Agents')
# plt.plot(times, mean_ag, color='pink', label='Mean Agents')
# plt.plot(times, mean_f, color='green', label='Mean Food')
# plt.legend()
#
# plt.savefig('Energy Loss')

# 3D PLOT OF GENESPACE

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.set_xlabel('Speed')
ax.set_ylabel('Size')
ax.set_zlabel('Angle')

ax.axes.set_xlim3d(left=0, right=100)
ax.axes.set_ylim3d(bottom=0, top=250)
ax.axes.set_zlim3d(bottom=0, top=5)

ax.scatter3D(speed1, size1, angle1, s=count1, color='blue', label=f'Prey:{pop1}')
ax.scatter3D(speedp1, sizep1, anglep1, s=countp1, color='red', label=f'Predator:{popp1}')

plt.legend(loc=0)
plt.savefig('3D Genespace - 1')

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.set_xlabel('Speed')
ax.set_ylabel('Size')
ax.set_zlabel('Angle')

ax.axes.set_xlim3d(left=0, right=120)
ax.axes.set_ylim3d(bottom=0, top=300)
ax.axes.set_zlim3d(bottom=0, top=5.5)

ax.scatter3D(speed2, size2, angle2, s=count2, color='blue', label=f'Prey:{pop2}')
ax.scatter3D(speedp2, sizep2, anglep2, s=countp2, color='red', label=f'Predator:{popp2}')

plt.legend(loc=0)
plt.savefig('3D Genespace - 2')

fig = plt.figure()
ax = plt.axes(projection='3d')


ax.set_xlabel('Speed')
ax.set_ylabel('Size')
ax.set_zlabel('Angle')

ax.axes.set_xlim3d(left=0, right=120)
ax.axes.set_ylim3d(bottom=0, top=300)
ax.axes.set_zlim3d(bottom=0, top=5)

ax.scatter3D(speed6, size6, angle6, s=count6, color='blue', label=f'Prey:{pop6}')
ax.scatter3D(speedp6, sizep6, anglep6, s=countp6, color='red', label=f'Predator:{popp6}')

plt.legend(loc=0)
plt.savefig('3D Genespace - 6')

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.set_xlabel('Speed')
ax.set_ylabel('Size')
ax.set_zlabel('Angle')

ax.axes.set_xlim3d(left=0, right=100)
ax.axes.set_ylim3d(bottom=0, top=220)
ax.axes.set_zlim3d(bottom=0, top=5)

ax.scatter3D(speed8, size8, angle8, s=count8, color='blue', label=f'Prey:{pop8}')
ax.scatter3D(speedp8, sizep8, anglep8, s=countp8, color='red', label=f'Predator:{popp8}')

plt.legend(loc=0)
plt.savefig('3D Genespace - 8')
plt.show()
