# 读写CSV文件
import sys
import csv

input_file = sys.argv[1]  # 在运行脚本时在命令行中输入的内容
output_file = sys.argv[2]
with open(input_file, 'r', newline='', encoding="utf-8") as csv_in_file:
    with open(output_file, 'w', newline='', encoding="utf-8") as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')
        for row_list in filereader:
            print(row_list)

