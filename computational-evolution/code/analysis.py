"""Analysis Module"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# import all data from folder

def importData(folder_path = 'computational-evolution/Data'):
    """Import all csv files, unpack into dataframes, and return dictionary"""

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    dataframes = {}

    for csv_file in csv_files:

        file_path = os.path.join(folder_path, csv_file)
        dataframes[csv_file.split('.')[0]] = pd.read_csv(file_path)
        
    return dataframes 


dataframes = importData()

print(dataframes['Agent_Data_49331'])


exit()

y1 = df_pop['Agent Population']
y2 = df_pop['Food Population']
x = df_pop['Time Elapsed/s']

plt.figure()

plt.plot(x, y1, 'go', markersize=1, label='Agent Population')
plt.plot(x, y2, 'ro', markersize=1, label='Food Population')


plt.legend()
plt.show()