import csv
import re
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)
with open(input_file, 'r', newline='', encoding='utf-8') as csv_in_file:
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            invoice_number = row_list[1]
            if pattern.search(invoice_number):
                filewriter.writerow(row_list)
                print(row_list)
