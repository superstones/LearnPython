prompt = "How old are you, please enter your age."
prompt += "\n Enter 'quit' to end the program. "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)
#     if age < 3:
#         print("You get in free.")
#     elif age >= 3 and age <= 12:
#         print("Your ticket is $10.")
#     else:
#         print("Your ticket is $15.")

# active = True
#
# while active:
#     age = input(prompt)
#     age = str(age)
#     if age == 'quit':
#         active = False
#     else:
#         age = int(age)
#         if age < 3:
#             print("You get in free.")
#         elif age >= 3 and age <= 12:
#             print("Your ticket is $10.")
#         else:
#             print("Your ticket is $15.")
#         break

while True:
    age = input(prompt)
    age = str(age)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("You get in free.")
        elif age >= 3 and age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
        break
