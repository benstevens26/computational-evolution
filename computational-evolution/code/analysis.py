"""Analysis Module

Functions:
    importData(): Import all csv files, unpack into dataframes, and return dictionary

"""

import pandas as pd
import os


def import_data(folder_path):
    """Import all csv files, unpack into dataframes, and return dictionary"""

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    dataframes = {}

    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        dataframes[csv_file.split('.')[0]] = pd.read_csv(file_path)

    return dataframes


ben_path = "computational-evolution/data"
dataframes = import_data(ben_path)


