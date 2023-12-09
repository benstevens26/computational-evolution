import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import analysis

# DATA SET 1

# df_data1 = pd.read_pickle('d1.pkl')
# # df_pop1 = pd.read_pickle('p1.pkl')
# # df_pred1 = pd.read_pickle('pr1.pkl')
#
# df_agent1 = df_data1[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
#
# big_angle = df_agent1[df_agent1['Angle'] >= 2]
# small_angle = df_agent1[df_agent1['Angle'] < 2]
#
# big_angle = big_angle.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# big_angle['Count'] = big_angle['Count'] * 50
# big_angle_speed = big_angle.groupby(['Time Elapsed/s'])['Speed'].mean().reset_index(name='Mean')
# big_angle_size = big_angle.groupby(['Time Elapsed/s'])['Size'].mean().reset_index(name='Mean')
# big_angle_angles = big_angle.groupby(['Time Elapsed/s'])['Angle'].mean().reset_index(name='Mean')
#
# big_angle_speed_sd = big_angle.groupby(['Time Elapsed/s'])['Speed'].std().reset_index(name='Sd')
# big_angle_size_sd = big_angle.groupby(['Time Elapsed/s'])['Size'].std().reset_index(name='Sd')
# big_angle_angles_sd = big_angle.groupby(['Time Elapsed/s'])['Angle'].std().reset_index(name='Sd')
#
# big_angle_count = big_angle.groupby(['Time Elapsed/s'])['Count'].apply(list)
#
# small_angle = small_angle.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# small_angle['Count'] = small_angle['Count'] * 50
# small_angle_speed = small_angle.groupby(['Time Elapsed/s'])['Speed'].mean().reset_index(name='Mean')
# small_angle_size = small_angle.groupby(['Time Elapsed/s'])['Size'].mean().reset_index(name='Mean')
# small_angle_angles = small_angle.groupby(['Time Elapsed/s'])['Angle'].mean().reset_index(name='Mean')
#
# small_angle_speed_sd = small_angle.groupby(['Time Elapsed/s'])['Speed'].std().reset_index(name='Sd')
# small_angle_size_sd = small_angle.groupby(['Time Elapsed/s'])['Size'].std().reset_index(name='Sd')
# small_angle_angles_sd = small_angle.groupby(['Time Elapsed/s'])['Angle'].std().reset_index(name='Sd')
#
# small_angle_count = small_angle.groupby(['Time Elapsed/s'])['Count'].apply(list)
#
# # Angle change
# plt.grid()
# plt.xlim(10000, 75000)
# plt.errorbar(big_angle_angles['Time Elapsed/s'], big_angle_angles['Mean'], yerr=big_angle_angles_sd['Sd'], fmt='x', color='orange')
# plt.errorbar(small_angle_angles['Time Elapsed/s'], small_angle_angles['Mean'], yerr=small_angle_angles_sd['Sd'], fmt='x', color='green')
# plt.show()


# times1 = df_pop1['Time Elapsed/s']
# # times1 = times1.iloc[::100]
#
# df_pred1 = df_pred1[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_pred1 = df_pred1.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
#
# df_pred1['Count'] = df_pred1['Count'] * 50
# df_speedp1 = df_pred1.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_sizep1 = df_pred1.groupby(['Time Elapsed/s'])['Size'].apply(list)
# countp1 = df_pred1.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_anglep1 = df_pred1.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# speedp1 = df_speedp1.iloc[::100]
# sizep1 = df_sizep1.iloc[::100]
# countp1 = countp1.iloc[::100]
# anglep1 = df_anglep1.iloc[::100]
#
# predator1 = [speedp1, sizep1, anglep1, countp1]
#
# anim = analysis.Animation(times1, prey1, predator1)  # mostly all the same size, but vary in eyesight angle
# anim.animate()

# DATA SET 2
# df_data2 = pd.read_pickle('d2.pkl')
# df_pop2 = pd.read_pickle('p2.pkl')
# df_pred2 = pd.read_pickle('pr2.pkl')
#
# df_agent2 = df_data2[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
#
# df_agent2 = df_agent2.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_agent2['Count'] = df_agent2['Count'] * 50
# df_speed2 = df_agent2.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size2 = df_agent2.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count2 = df_agent2.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_angle2 = df_agent2.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# df_speed2 = df_speed2.iloc[::100]  # Every 100 frames
# df_size2 = df_size2.iloc[::100]
# count2 = count2.iloc[::100]
# df_angle2 = df_angle2.iloc[::100]
#
# prey2 = [df_speed2, df_size2, df_angle2, count2]
#
# times2 = df_pop2['Time Elapsed/s']
# times2 = times2.iloc[::100]
#
# df_pred2 = df_pred2[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_pred2 = df_pred2.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
#
# df_pred2['Count'] = df_pred2['Count'] * 50
# df_speedp2 = df_pred2.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_sizep2 = df_pred2.groupby(['Time Elapsed/s'])['Size'].apply(list)
# countp2 = df_pred2.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_anglep2 = df_pred2.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# speedp2 = df_speedp2.iloc[::100]
# sizep2 = df_sizep2.iloc[::100]
# countp2 = countp2.iloc[::100]
# anglep2 = df_anglep2.iloc[::100]
#
# predator2 = [speedp2, sizep2, anglep2, countp2]
#
# anim = analysis.Animation(times2, prey2, predator2)  # not much difference between predators and prey, prey slightly faster
# anim.animate()

#
# # DATA SET 4
# df_data4 = pd.read_pickle('d4.pkl')
# df_pop4 = pd.read_pickle('p4.pkl')
# df_pred4 = pd.read_pickle('pr4.pkl')
#
# df_agent4 = df_data4[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
#
# df_agent4 = df_agent4.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_agent4['Count'] = df_agent4['Count'] * 50
# df_speed4 = df_agent4.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size4 = df_agent4.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count4 = df_agent4.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_angle4 = df_agent4.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# speed4 = df_speed4.iloc[::100]
# size4 = df_size4.iloc[::100]
# count4 = count4.iloc[::100]
# angle4 = df_angle4.iloc[::100]
#
# prey4 = [speed4, size4, angle4, count4]
#
# times4 = df_pop4['Time Elapsed/s']
# times4 = times4.iloc[::100]
#
# df_pred4 = df_pred4[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_pred4 = df_pred4.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
#
# df_pred4['Count'] = df_pred4['Count'] * 50
# df_speedp4 = df_pred4.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_sizep4 = df_pred4.groupby(['Time Elapsed/s'])['Size'].apply(list)
# countp4 = df_pred4.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_anglep4 = df_pred4.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# speedp4 = df_speedp4.iloc[::100]
# sizep4 = df_sizep4.iloc[::100]
# countp4 = countp4.iloc[::100]
# anglep4 = df_anglep4.iloc[::100]
#
# predator4 = [sizep4, speedp4, anglep4, countp4]
#
# anim = analysis.Animation(times4, prey4, predator4) # predator speciation seen, prey faster and smaller
# anim.animate()

#
# # DATA SET 8
# df_data8 = pd.read_pickle('d8.pkl')
# df_pop8 = pd.read_pickle('p8.pkl')
# df_pred8 = pd.read_pickle('pr8.pkl')
#
# df_agent8 = df_data8[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
#
# df_agent8 = df_agent8.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_agent8['Count'] = df_agent8['Count'] * 50
# df_speed8 = df_agent8.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size8 = df_agent8.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count8 = df_agent8.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_angle8 = df_agent8.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# speed8 = df_speed8.iloc[::100]
# size8 = df_size8.iloc[::100]
# count8 = count8.iloc[::100]
# angle8 = df_angle8.iloc[::100]
#
# prey8 = [speed8, size8, angle8, count8]
#
# times8 = df_pop8['Time Elapsed/s']
# times8 = times8.iloc[::100]
#
# df_pred8 = df_pred8[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_pred8 = df_pred8.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
#
# df_pred8['Count'] = df_pred8['Count'] * 50
# df_speedp8 = df_pred8.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_sizep8 = df_pred8.groupby(['Time Elapsed/s'])['Size'].apply(list)
# countp8 = df_pred8.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_anglep8 = df_pred8.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# speedp8 = df_speedp8.iloc[::100]
# sizep8 = df_sizep8.iloc[::100]
# countp8 = countp8.iloc[::100]
# anglep8 = df_anglep8.iloc[::100]
#
# predator8 = [speedp8, sizep8, anglep8, countp8]
#
# anim = analysis.Animation(times8, prey8, predator8)
# anim.animate()

#
# # DATA SET 9
# df_data9 = pd.read_pickle('d9.pkl')
# df_pop9 = pd.read_pickle('p9.pkl')
# df_pred9 = pd.read_pickle('pr9.pkl')
#
# df_agent9 = df_data9[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
#
# df_agent9 = df_agent9.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_agent9['Count'] = df_agent9['Count'] * 50
# df_speed9 = df_agent9.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size9 = df_agent9.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count9 = df_agent9.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_angle9 = df_agent9.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# speed9 = df_speed9.iloc[::100]
# size9 = df_size9.iloc[::100]
# count9 = count9.iloc[::100]
# angle9 = df_angle9.iloc[::100]
#
# prey9 = [speed9, size9, angle9, count9]
#
# times9 = df_pop9['Time Elapsed/s']
# times9 = times9.iloc[::100]
#
# df_pred9 = df_pred9[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
# df_pred9 = df_pred9.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
#
# df_pred9['Count'] = df_pred9['Count'] * 50
# df_speedp9 = df_pred9.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_sizep9 = df_pred9.groupby(['Time Elapsed/s'])['Size'].apply(list)
# countp9 = df_pred9.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_anglep9 = df_pred9.groupby(['Time Elapsed/s'])['Angle'].apply(list)
#
# speedp9 = df_speedp9.iloc[::100]
# sizep9 = df_sizep9.iloc[::100]
# countp9 = countp9.iloc[::100]
# anglep9 = df_anglep9.iloc[::100]
#
# predator9 = [speedp9, sizep9, anglep9, countp9]
#
# anim = analysis.Animation(times9, prey9, predator9)  # speciation of elephants + gazelles seen but gazelles died out
# anim.animate()