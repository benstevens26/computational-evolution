"""Analysis Module

Functions:
    importData(): Import all csv files, unpack into dataframes, and return dictionary

"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pickle


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

    def __init__(self, times, speed, population, count, size):
        self.fig = plt.figure('Genespace', figsize=(6, 6))
        self.ax = plt.axes(xlim=(0, 200), ylim=(0, 200))

        self.times = times
        self.speeds = speed
        self.population = population
        self.sizes = size
        self.counts = count

    def update(self, i):
        self.ax.clear()

        self.ax.set_xlim(0, 200)
        self.ax.set_ylim(0, 200)
        self.ax.set_xlabel('Speed')
        self.ax.set_ylabel('Size')

        self.step_text1 = self.ax.text(0.4 * 200, 1.01 * 200, '')
        self.pop_text1 = self.ax.text(0.7 * 200, 1.01 * 200, '')
        self.fig_title = self.ax.text(0.35 * 200, 1.05 * 200, 'Genespace')

        self.ax.scatter(self.speeds.iloc[i], self.sizes.iloc[i], s=self.counts.iloc[i])
        self.step_text1.set_text('Steps: ' + str(self.times.iloc[i]))
        self.pop_text1.set_text('Population: ' + str(self.population.iloc[i]))

    def animate(self):
        anim = animation.FuncAnimation(self.fig, self.update, frames=len(self.times), interval=0.1, repeat=False)

        plt.show()