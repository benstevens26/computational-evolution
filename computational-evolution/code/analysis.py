"""Analysis Module

Functions:
    importData(): Import all csv files, unpack into dataframes, and return dictionary

"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def import_data(folder_path):
    """Import all csv files, unpack into dataframes, and return dictionary"""

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    dataframes = {}

    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        dataframes[csv_file.split('.')[0]] = pd.read_csv(file_path)

    return dataframes


# ben_path = "computational-evolution/data"
# dataframes = import_data(ben_path)


class Animation:

    def __init__(self, times, agents1, agents2, agents3, predators): #agents2, agents3, predators
        self.fig = plt.figure('Genespace', figsize=(6, 6))
        self.ax = plt.axes(projection='3d', xlim=(0, 200), ylim=(0, 200), zlim=(0, 5))

        speed1, size1, angle1, count1 = agents1
        speed2, size2, angle2, count2 = agents2
        speed3, size3, angle3, count3 = agents3
        speedp, sizep, anglep, countp = predators

        self.times = times
        self.speeds1 = speed1
        self.sizes1 = size1
        self.counts1 = count1
        self.angle1 = angle1

        self.speeds2 = speed2
        self.sizes2 = size2
        self.counts2 = count2
        self.angle2 = angle2

        self.speeds3 = speed3
        self.sizes3 = size3
        self.counts3 = count3
        self.angle3 = angle3

        self.speedsp = speedp
        self.sizesp = sizep
        self.countsp = countp
        self.anglep = anglep

    def update(self, i):
        self.ax.clear()

        self.ax.set_xlim(0, 200)
        self.ax.set_ylim(0, 200)
        self.ax.set_zlim(0, 5)
        self.ax.set_xlabel('Size')
        self.ax.set_ylabel('Speed')
        self.ax.set_zlabel('Angle')

        self.step_text1 = self.ax.text(0.5 * 200, 1.03 * 200, 6, 'Steps: ' + str(self.times.iloc[i]))
        self.fig_title = self.ax.text(0.5 * 200, 1.2 * 200, 7, 'Genespace')

        if i > (len(self.sizes1) - 1):
            print('no elephants')

        else:
            self.ax.scatter3D(self.sizes1.iloc[i], self.speeds1.iloc[i], self.angle1.iloc[i], s=self.counts1.iloc[i],
                              color='mediumpurple', label='Elephant')
            self.pop_text1 = self.ax.text(0.9 * 200, 1.02 * 200, 6, 'Elephant:' + str(len(self.speeds1.iloc[i])))

        if i > (len(self.sizes2) - 1):
            print('no gazelles')

        else:
            self.ax.scatter3D(self.sizes2.iloc[i], self.speeds2.iloc[i], self.angle2.iloc[i], s=self.counts2.iloc[i],
                              color='darkorange', label='Gazelles')
            self.pop_text2 = self.ax.text(0.9 * 200, 1.07 * 200, 6.6, 'Gazelles:' + str(len(self.speeds2.iloc[i])))

        if i > (len(self.sizes3) - 1):
            print('speciation occurred')

        else:
            self.ax.scatter3D(self.sizes3.iloc[i], self.speeds3.iloc[i], self.angle3.iloc[i], s=self.counts3.iloc[i],
                              color='cornflowerblue', label='Prey')
            self.pop_text3 = self.ax.text(0.1 * 200, 1.01 * 200, 6.5, 'Prey:' + str(len(self.speeds3.iloc[i])))

        if i > (len(self.sizesp) - 1):
            print('no more predators')
        else:
            self.ax.scatter3D(self.sizesp.iloc[i], self.speedsp.iloc[i], self.anglep.iloc[i], s=self.countsp.iloc[i],
                              color='salmon', label='Predators')
            self.pop_text1 = self.ax.text(0.1 * 200, 1.01 * 200, 6, 'Predators:' + str(len(self.speedsp.iloc[i])))

        plt.legend(loc=2)

    def animate(self):
        anim = animation.FuncAnimation(self.fig, self.update, frames=len(self.times), interval=0.05, repeat=False)
        #plt.show()
        anim.save('elephant_gazelle.gif')
