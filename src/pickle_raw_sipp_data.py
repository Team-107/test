import pandas as pd
import os
from datetime import datetime

desired_width = 320
pd.set_option('display.width', desired_width)

import numpy as np

start_time = datetime.now()


#Read in the primary data

current_working_direc = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_working_direc, os.pardir))
data_dir = os.path.join(parent_dir, "data")
raw_data_dir = os.path.join(data_dir, "raw")
sipp_data_dir = os.path.join(raw_data_dir, "sipp_2018")
sipp_data_path = os.path.join(sipp_data_dir, "pu2018.csv")


#df_data = pd.read_csv(sipp_data_path, sep='|', header=0)
"""
chunk = pd.read_csv(sipp_data_path,
                    header=0,
                    sep="|",
                    chunksize=10**5,
                    engine='c',
                    nrows=5000)
df = pd.concat(chunk)
"""
columns_to_use = []
partial_df = pd.read_csv(sipp_data_path,
                            header=0,
                            sep="|",
                            memory_map=True,
                            #chunksize=10**5,
                            na_filter=False,
                            engine='c',
                            nrows=10000)

end_time = datetime.now()
duration = end_time - start_time
print('Duration: {}'.format(duration))
print(partial_df.head(25))
partial_df.to_csv("partial_df.csv")