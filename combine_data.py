'''
This file combines all the data to a single dataframe
'''

import pandas as pd
import os

class CSVData:
    def __init__(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".csv"):
                var_name = os.path.splitext(filename)[0].replace(" ", "_").replace("-", "_")
                df = pd.read_csv(os.path.join(folder_path, filename))
                setattr(self, var_name, df)

# Usage
folder_path = "data/Folder_1/dataset"
data = CSVData(folder_path)

print(data.dailyActivity_merged)

