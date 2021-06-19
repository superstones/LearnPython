# 10.3访客
guest_name = input("Please enter your name: ")
file_name = 'guest.txt'
with open(file_name, 'a') as file_object:
    file_object.write(guest_name + "\n")
