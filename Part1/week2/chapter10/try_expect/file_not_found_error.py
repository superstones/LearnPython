# file_name = 'alice.txt'
#
# with open(file_name) as file_object:
#     contents = file_object.read()

file_name = 'alice.txt'
try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + "does not exist."
    print(msg)
