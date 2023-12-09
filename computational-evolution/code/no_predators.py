import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import analysis

# FIRST DATASET
# df_data_prey = pd.read_pickle('d_nop.pkl')
# df_pop_prey = pd.read_pickle('p_nop.pkl')
#
# df_data_prey = df_data_prey[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_data_prey = df_data_prey.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_data_prey['Count'] = df_data_prey['Count']*50
# df_prey_speed = df_data_prey.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_prey_size = df_data_prey.groupby(['Time Elapsed/s'])['Size'].apply(list)
# df_prey_angle = df_data_prey.groupby(['Time Elapsed/s'])['Angle'].apply(list)
# df_prey_count = df_data_prey.groupby(['Time Elapsed/s'])['Count'].apply(list)
#
# df_prey_speed = df_prey_speed.iloc[::100]
# df_prey_size = df_prey_size.iloc[::100]
# df_prey_angle = df_prey_angle.iloc[::100]
# df_prey_count = df_prey_count.iloc[::100]
#
# prey = [df_prey_speed, df_prey_size, df_prey_angle, df_prey_count]
#
# times = df_pop_prey['Time Elapsed/s']
# times = times.iloc[::100]
#
# anim = analysis.Animation(times, prey)
# anim.animate()

# SECOND DATASET
# df_data_prey_1 = pd.read_pickle('d_nop1.pkl')
# df_pop_prey_1 = pd.read_pickle('p_nop1.pkl')
#
# df_data_prey_1 = df_data_prey_1[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_data_prey_1 = df_data_prey_1.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_data_prey_1['Count'] = df_data_prey_1['Count']*50
# df_prey_speed_1 = df_data_prey_1.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_prey_size_1 = df_data_prey_1.groupby(['Time Elapsed/s'])['Size'].apply(list)
# df_prey_angle_1 = df_data_prey_1.groupby(['Time Elapsed/s'])['Angle'].apply(list)
# df_prey_count_1 = df_data_prey_1.groupby(['Time Elapsed/s'])['Count'].apply(list)
#
# df_prey_speed_1 = df_prey_speed_1.iloc[::100]
# df_prey_size_1 = df_prey_size_1.iloc[::100]
# df_prey_angle_1 = df_prey_angle_1.iloc[::100]
# df_prey_count_1 = df_prey_count_1.iloc[::100]
#
# prey1 = [df_prey_speed_1, df_prey_size_1, df_prey_angle_1, df_prey_count_1]
#
# times1 = df_pop_prey_1['Time Elapsed/s']
# times1 = times1.iloc[::100]
#
# anim = analysis.Animation(times1, prey1)
# anim.animate()

# THIRD DATA SET
# df_data_prey_2 = pd.read_pickle('d_nop2.pkl')
# df_pop_prey_2 = pd.read_pickle('p_nop2.pkl')
#
# df_data_prey_2 = df_data_prey_2[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_data_prey_2 = df_data_prey_2.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_data_prey_2['Count'] = df_data_prey_2['Count']*50
# df_prey_speed_2 = df_data_prey_2.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_prey_size_2 = df_data_prey_2.groupby(['Time Elapsed/s'])['Size'].apply(list)
# df_prey_angle_2 = df_data_prey_2.groupby(['Time Elapsed/s'])['Angle'].apply(list)
# df_prey_count_2 = df_data_prey_2.groupby(['Time Elapsed/s'])['Count'].apply(list)
#
# df_prey_speed_2 = df_prey_speed_2.iloc[::100]
# df_prey_size_2 = df_prey_size_2.iloc[::100]
# df_prey_angle_2 = df_prey_angle_2.iloc[::100]
# df_prey_count_2 = df_prey_count_2.iloc[::100]
#
# prey2 = [df_prey_speed_2, df_prey_size_2, df_prey_angle_2, df_prey_count_2]
#
# times2 = df_pop_prey_2['Time Elapsed/s']
# times2 = times2.iloc[::100]
#
# anim = analysis.Animation(times2, prey2)
# anim.animate()

# FOURTH DATASET
df_data_prey_3 = pd.read_pickle('d_nop3.pkl')
df_pop_prey_3 = pd.read_pickle('p_nop3.pkl')

df_data_prey_3 = df_data_prey_3[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
df_data_prey_3 = df_data_prey_3.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
df_data_prey_3['Count'] = df_data_prey_3['Count']*50
df_prey_speed_3 = df_data_prey_3.groupby(['Time Elapsed/s'])['Speed'].apply(list)
df_prey_size_3 = df_data_prey_3.groupby(['Time Elapsed/s'])['Size'].apply(list)
df_prey_angle_3 = df_data_prey_3.groupby(['Time Elapsed/s'])['Angle'].apply(list)
df_prey_count_3 = df_data_prey_3.groupby(['Time Elapsed/s'])['Count'].apply(list)

df_prey_speed_3 = df_prey_speed_3.iloc[::100]
df_prey_size_3 = df_prey_size_3.iloc[::100]
df_prey_angle_3 = df_prey_angle_3.iloc[::100]
df_prey_count_3 = df_prey_count_3.iloc[::100]

prey3 = [df_prey_speed_3, df_prey_size_3, df_prey_angle_3, df_prey_count_3]

times3 = df_pop_prey_3['Time Elapsed/s']
times3 = times3.iloc[::100]

anim = analysis.Animation(times3, prey3)
anim.animate()