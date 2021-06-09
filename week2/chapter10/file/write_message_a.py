file_name = 'programming.txt'
with open(file_name, 'a') as file_object:  # 'a为附加模式，写入文件的行都将添加到文件末尾
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
