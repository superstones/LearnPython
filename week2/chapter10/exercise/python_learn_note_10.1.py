# 10.1Python学习笔记
file_name = 'learning_python.txt'
with open(file_name) as file_object:
    contents = file_object.read()
    print(contents)

with open(file_name) as file_object:
    for line in file_object.readlines():
        print(line.rstrip())
print('\n')
pi_string = ''
with open(file_name) as file_object:
    for line in file_object.readlines():
        pi_string += line
print(pi_string)


