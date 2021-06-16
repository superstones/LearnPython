# 10.8&10.9猫和狗

def realize_file(file_name):
    try:
        with open(file_name, 'r') as f:
            contents = f.readlines()
    except FileNotFoundError:
        pass
        # msg = "Sorry, the file " + file_name + " does not exist."
        # print(msg)
    else:
        for line in contents:
            print(line.rstrip())


file_names = ['cats.txt', 'dogs.txt', 'human.txt']
for file_name in file_names:
    realize_file(file_name)
