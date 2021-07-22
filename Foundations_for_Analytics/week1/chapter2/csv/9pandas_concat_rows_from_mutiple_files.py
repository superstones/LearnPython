import pandas as pd
import glob
import os

input_path = 'D:\LearnPython\Foundations_for_Analytics\week1\chapter2\csv'
output_file = '13pd_output.csv'
all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []
for file in all_files:
    data_frame = pd.read_csv(file, index_col=None)
    all_data_frames.append(data_frame)
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index=False)
