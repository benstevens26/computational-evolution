import matplotlib.pyplot as plt
import pandas as pd
import analysis

df_data6 = pd.read_pickle('d6.pkl')
df_pop6 = pd.read_pickle('p6.pkl')
df_pred6 = pd.read_pickle('pr6.pkl')

df_agent6 = df_data6[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]

elephants = df_agent6[df_agent6['Size'] >= 125]
gazelles = df_agent6[df_agent6['Size'] <= 100]
prey = df_agent6[df_agent6['Size'].between(100, 125)]

# ELEPHANT DATA
elephants = elephants.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
elephants['Count'] = elephants['Count'] * 50
elephant_speed = elephants.groupby(['Time Elapsed/s'])['Speed'].apply(list)
elephant_size = elephants.groupby(['Time Elapsed/s'])['Size'].apply(list)
elephant_count = elephants.groupby(['Time Elapsed/s'])['Count'].apply(list)
elephant_angle = elephants.groupby(['Time Elapsed/s'])['Angle'].apply(list)
elephant_speed = elephant_speed.iloc[::500]
elephant_size = elephant_size.iloc[::500]
elephant_angle = elephant_angle.iloc[::500]
elephant_count = elephant_count.iloc[::500]
elephant = [elephant_speed, elephant_size, elephant_angle, elephant_count]

# GAZELLE DATA
gazelles = gazelles.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
gazelles['Count'] = gazelles['Count'] * 50
gazelle_speed = gazelles.groupby(['Time Elapsed/s'])['Speed'].apply(list)
gazelle_size = gazelles.groupby(['Time Elapsed/s'])['Size'].apply(list)
gazelle_count = gazelles.groupby(['Time Elapsed/s'])['Count'].apply(list)
gazelle_angle = gazelles.groupby(['Time Elapsed/s'])['Angle'].apply(list)
gazelle_speed = gazelle_speed.iloc[::500]
gazelle_size = gazelle_size.iloc[::500]
gazelle_angle = gazelle_angle.iloc[::500]
gazelle_count = gazelle_count.iloc[::500]
gazelle = [gazelle_speed, gazelle_size, gazelle_angle, gazelle_count]

# PREY DATA
prey = prey.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')
prey['Count'] = prey['Count'] * 50
prey_speed = prey.groupby(['Time Elapsed/s'])['Speed'].apply(list)
prey_size = prey.groupby(['Time Elapsed/s'])['Size'].apply(list)
prey_count = prey.groupby(['Time Elapsed/s'])['Count'].apply(list)
prey_angle = prey.groupby(['Time Elapsed/s'])['Angle'].apply(list)
prey_speed = prey_speed.iloc[::500]
prey_size = prey_size.iloc[::500]
prey_angle = prey_angle.iloc[::500]
prey_count = prey_count.iloc[::500]
prey = [prey_speed, prey_size, prey_angle, prey_count]

population6 = df_pop6['Agent Population']
times6 = df_pop6['Time Elapsed/s']

# population6 = population6.iloc[::100]
times6 = times6.iloc[::500]
# speed6 = df_speed6.iloc[-1]
# size6 = df_size6.iloc[-1]
# count6 = count6.iloc[-1]
# pop6 = population6.iloc[-1]
# angle6 = df_angle6.iloc[-1]

df_pred6 = df_pred6[['Time Elapsed/s', 'Speed', 'Size', 'Angle']]
df_pred6 = df_pred6.groupby(['Time Elapsed/s', 'Speed', 'Size', 'Angle']).size().reset_index(name='Count')

df_pred6['Count'] = df_pred6['Count'] * 50
df_speedp6 = df_pred6.groupby(['Time Elapsed/s'])['Speed'].apply(list)
df_sizep6 = df_pred6.groupby(['Time Elapsed/s'])['Size'].apply(list)
countp6 = df_pred6.groupby(['Time Elapsed/s'])['Count'].apply(list)
df_anglep6 = df_pred6.groupby(['Time Elapsed/s'])['Angle'].apply(list)

df_sizep6 = df_sizep6.iloc[::500]
df_speedp6 = df_speedp6.iloc[::500]
df_anglep6 = df_anglep6.iloc[::500]
countp6 = countp6.iloc[::500]
predator = [df_speedp6, df_sizep6, df_anglep6, countp6]


# speedp6 = df_speedp6.iloc[-1]
# sizep6 = df_sizep6.iloc[-1]
# countp6 = countp6.iloc[-1]
# anglep6 = df_anglep6.iloc[-1]
# popp6 = len(speedp6)

anim = analysis.Animation(times6, elephant, gazelle, prey, predator)
anim.animate()

# fig = plt.figure()
# ax = plt.axes(projection='3d')
#
# ax.set_xlabel('Speed')
# ax.set_ylabel('Size')
# ax.set_zlabel('Angle')
#
# # ax.axes.set_xlim3d(left=0, right=120)
# # ax.axes.set_ylim3d(bottom=0, top=300)
# # ax.axes.set_zlim3d(bottom=0, top=5)
#
# ax.scatter3D(speed6, size6, angle6, s=count6, color='blue', label=f'Prey:{pop6}')
# ax.scatter3D(speedp6, sizep6, anglep6, s=countp6, color='red', label=f'Predator:{popp6}')
#
# plt.legend(loc=0)
# plt.show()

# MEAN GENES + PLOTS
# gazelle_speed_mean = (gazelles.groupby(['Time Elapsed/s'])['Speed'].mean().reset_index(name='Mean')).iloc[::1000]
# gazelle_size_mean = (gazelles.groupby(['Time Elapsed/s'])['Size'].mean().reset_index(name='Mean')).iloc[::1000]
# gazelle_angle_mean = (gazelles.groupby(['Time Elapsed/s'])['Angle'].mean().reset_index(name='Mean')).iloc[::1000]
#
# gazelle_speed_sd = (gazelles.groupby(['Time Elapsed/s'])['Speed'].std().reset_index(name='Sd')).iloc[::1000]
# gazelle_size_sd = (gazelles.groupby(['Time Elapsed/s'])['Size'].std().reset_index(name='Sd')).iloc[::1000]
# gazelle_angle_sd = (gazelles.groupby(['Time Elapsed/s'])['Angle'].std().reset_index(name='Sd')).iloc[::1000]
#
# elephant_speed_mean = (elephants.groupby(['Time Elapsed/s'])['Speed'].mean().reset_index(name='Mean')).iloc[::1000]
# elephant_size_mean = (elephants.groupby(['Time Elapsed/s'])['Size'].mean().reset_index(name='Mean')).iloc[::1000]
# elephant_angle_mean = (elephants.groupby(['Time Elapsed/s'])['Angle'].mean().reset_index(name='Mean')).iloc[::1000]
#
# elephant_speed_sd = (elephants.groupby(['Time Elapsed/s'])['Speed'].std().reset_index(name='Sd')).iloc[::1000]
# elephant_size_sd = (elephants.groupby(['Time Elapsed/s'])['Size'].std().reset_index(name='Sd')).iloc[::1000]
# elephant_angle_sd = (elephants.groupby(['Time Elapsed/s'])['Angle'].std().reset_index(name='Sd')).iloc[::1000]
# #
# plt.figure(figsize=[7, 5])
# plt.grid()
# plt.title('Size Evolution')
# plt.xlabel('Time Elapsed/s')
# plt.ylabel('Mean Size')
# plt.ylim(0, 250)
#
# plt.errorbar(gazelle_size_mean['Time Elapsed/s'], gazelle_size_mean['Mean'], yerr=gazelle_size_sd['Sd'], fmt='x',
#              color='darkorange', label='Gazelles', capsize=2)
# plt.errorbar(elephant_size_mean['Time Elapsed/s'], elephant_size_mean['Mean'], yerr=elephant_size_sd['Sd'], fmt='x',
#              color='mediumpurple', label='Elephants', capsize=2)
# plt.legend()
# plt.savefig('Mean Size')
#
# plt.figure(figsize=[7, 5])
# plt.grid()
# #plt.tight_layout()
# plt.title('Speed Evolution')
# plt.xlabel('Time Elapsed/s')
# plt.ylabel('Mean Speed')
# plt.ylim(0, 150)
#
# plt.errorbar(gazelle_speed_mean['Time Elapsed/s'], gazelle_speed_mean['Mean'], yerr=gazelle_speed_sd['Sd'], fmt='x',
#              color='darkorange', label='Gazelles', capsize=2)
# plt.errorbar(elephant_speed_mean['Time Elapsed/s'], elephant_speed_mean['Mean'], yerr=elephant_speed_sd['Sd'], fmt='x',
#              color='mediumpurple', label='Elephants', capsize=2)
# plt.legend()
#
# plt.savefig('Mean Speed')
# #
# plt.figure(figsize=[7, 5])
# plt.grid()
# plt.title('Angle Evolution')
# plt.xlabel('Time Elapsed/s')
# plt.ylabel('Mean Angle')
# plt.ylim(0, 5)
#
# plt.errorbar(gazelle_angle_mean['Time Elapsed/s'], gazelle_angle_mean['Mean'], yerr=gazelle_angle_sd['Sd'], fmt='x',
#              color='darkorange', label='Gazelles', capsize=2)
# plt.errorbar(elephant_angle_mean['Time Elapsed/s'], elephant_angle_mean['Mean'], yerr=elephant_angle_sd['Sd'], fmt='x',
#              color='mediumpurple', label='Elephants', capsize=2)
# plt.legend()
# plt.savefig('Mean Angle')
