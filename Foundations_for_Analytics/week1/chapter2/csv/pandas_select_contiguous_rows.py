import pandas as pd

input_file = 'supplier_data.csv'
output_file = '11output_pd.csv'
data_frame = pd.read_csv(input_file, header=None)
data_frame = data_frame.drop([0, 1, 2, 16, 17, 18])
print(data_frame.values)
data_frame.columns = data_frame.iloc[0]
print(data_frame.columns)
print(data_frame)
data_frame = data_frame.reindex(data_frame.index.drop(3))
print(data_frame.index)
data_frame.to_csv(output_file, index=False)
