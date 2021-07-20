import pandas as pd

input_file = 'supplier_data.csv'
output_file = '12pandas_output.csv'
header_list = ['Supplier Name', 'Invoice Number', 'Part number', 'Cost', 'Purchase Date']
data_frame = pd.read_csv(input_file, header=None, names=header_list)
data_frame.to_csv(output_file, index=False)
