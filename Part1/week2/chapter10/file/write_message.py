# 写入空文件
file_name = 'programming.txt'

with open(file_name, 'w') as file_object:  # 如果写入的文件不存在，函数open()将自动创建它，
    # 但以写入('w')模式打开文件时，如果指定的文件已经存在，Python将在返回文件对象前清空该文件
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

