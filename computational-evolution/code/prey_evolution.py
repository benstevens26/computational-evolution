import pandas as pd
import analysis
import matplotlib.pyplot as plt

df_data3 = pd.read_pickle('d3.pkl')
# df_pop3 = pd.read_pickle('p3.pkl')
# df_pred3 = pd.read_pickle('pr3.pkl')

df_agent3 = df_data3[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]

# df_agent3 = df_agent3.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
# df_agent3['Count'] = df_agent3['Count'] * 50
# df_speed3 = df_agent3.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_size3 = df_agent3.groupby(['Time Elapsed/s'])['Size'].apply(list)
# count3 = df_agent3.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_angle3 = df_agent3.groupby(['Time Elapsed/s'])['Angle'].apply(list)

# df_speed3 = df_speed3.iloc[::100]
# df_size3 = df_size3.iloc[::100]
# df_angle3 = df_angle3.iloc[::100]
# count3 = count3.iloc[::100]
#
# prey = [df_speed3, df_size3, df_angle3, count3]
#
# population3 = df_pop3['Agent Population']
# times3 = df_pop3['Time Elapsed/s']

# population3 = population3.iloc[::100]
# times3 = times3.iloc[::100]
# speed3 = df_speed3.iloc[-1]
# size3 = df_size3.iloc[-1]
# count3 = count3.iloc[-1]
# pop3 = population3.iloc[-1]
# angle3 = df_angle3.iloc[-1]

# speed = df_speed3.iloc[11000]
# size = df_size3.iloc[11000]

# mean_size = sum(size3) / len(size3)
# mean_speed = sum(speed3) / len(speed3)
#
# mean_sizeb = sum(size) / len(size)
# mean_speedb = sum(speed) / len(speed)
#
# print(mean_size, mean_sizeb, mean_speed, mean_speedb)

# df_pred3 = df_pred3[['Time Elapsed/s', 'Speed', 'Size', 'Angle']] # die off at 11290
# print(df_pred3.iloc[-1])
# df_pred3 = df_pred3.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')

# df_pred3['Count'] = df_pred3['Count'] * 50
# df_speedp3 = df_pred3.groupby(['Time Elapsed/s'])['Speed'].apply(list)
# df_sizep3 = df_pred3.groupby(['Time Elapsed/s'])['Size'].apply(list)
# countp3 = df_pred3.groupby(['Time Elapsed/s'])['Count'].apply(list)
# df_anglep3 = df_pred3.groupby(['Time Elapsed/s'])['Angle'].apply(list)

# df_sizep3 = df_sizep3.iloc[::100]
# df_speedp3 = df_speedp3.iloc[::100]
# df_anglep3 = df_anglep3.iloc[::100]
# countp3 = countp3.iloc[::100]
# predator = [df_speedp3, df_sizep3, df_anglep3, countp3]

 #speedp3 = df_speedp3.iloc[-1]
#
# sizep3 = df_sizep3.iloc[-1]
# countp3 = countp3.iloc[-1]
# anglep3 = df_anglep3.iloc[-1]
# popp3 = len(speedp3)

# anim = analysis.Animation(times3, prey, predator)
# anim.animate()

# speed_mean = (df_agent3.groupby(['Time Elapsed/s'])['Speed'].mean().reset_index(name='Mean')).iloc[::1000]
# size_mean = (df_agent3.groupby(['Time Elapsed/s'])['Size'].mean().reset_index(name='Mean')).iloc[::1000]
# angle_mean = (df_agent3.groupby(['Time Elapsed/s'])['Angle'].mean().reset_index(name='Mean')).iloc[::1000]
#
# speed_sd = (df_agent3.groupby(['Time Elapsed/s'])['Speed'].std().reset_index(name='Sd')).iloc[::1000]
# size_sd = (df_agent3.groupby(['Time Elapsed/s'])['Size'].std().reset_index(name='Sd')).iloc[::1000]
# angle_sd = (df_agent3.groupby(['Time Elapsed/s'])['Angle'].std().reset_index(name='Sd')).iloc[::1000]
#
# plt.figure(figsize=[7, 5])
# plt.grid()
# plt.title('Angle Evolution')
# plt.xlabel('Time Elapsed/s')
# plt.ylabel('Mean Angle')
# plt.ylim(0, 6)
#
# plt.errorbar(angle_mean['Time Elapsed/s'], angle_mean['Mean'], yerr=angle_sd['Sd'], fmt='x',
#              color='mediumpurple', capsize=2)
# plt.axvline(x=11290, color='black', linestyle='dashed', label='No Predators')
# plt.legend()
# plt.savefig('Angle - No Pred')
#
# plt.figure(figsize=[7, 5])
# plt.grid()
# plt.title('Speed Evolution')
# plt.xlabel('Time Elapsed/s')
# plt.ylabel('Mean Speed')
# plt.ylim(0, 180)
#
# plt.errorbar(speed_mean['Time Elapsed/s'], speed_mean['Mean'], yerr=speed_sd['Sd'], fmt='x',
#              color='mediumpurple', capsize=2)
# plt.axvline(x=11290, color='black', linestyle='dashed', label='No Predators')
# plt.legend()
# plt.savefig('Speed - No Pred')
# #
# plt.figure(figsize=[7, 5])
# plt.grid()
# plt.title('Size Evolution')
# plt.xlabel('Time Elapsed/s')
# plt.ylabel('Mean Size')
# plt.ylim(0, 140)
#
# plt.errorbar(size_mean['Time Elapsed/s'], size_mean['Mean'], yerr=size_sd['Sd'], fmt='x',
#              color='mediumpurple', capsize=2)
# plt.axvline(x=11290, color='black', linestyle='dashed', label='No Predators')
# plt.legend()
# plt.savefig('Size - No Pred')