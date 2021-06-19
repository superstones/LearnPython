# 10.4访客名单
prompt = "\nPlease enter your name:  "
prompt += "\n(Enter 'q' to quit.)"

file_name = 'guest_book.txt'
while True:
    guest_name = input(prompt)
    if guest_name == 'q':
        break
    else:
        with open(file_name, 'a') as file_object:
            file_object.write(guest_name + "\n")
            print("Hello," + guest_name)
