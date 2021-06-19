# 7.6三个出口
prompt = "How old are you? Please enter your age. "
prompt += "\nEnter 'quit' when you are finished. "

# 使用while循环中使用条件测试来结束循环
# age = input(prompt)
# age = str(age)
# while True:
#     if age == 'quit':
#         break
#     elif int(age) < 3:
#         print("Free")
#     elif int(age) >= 3 and int(age) <= 12:
#         print("Your ticket price is $10")
#     else:
#         print("Your ticket price is $15")
#     break

active = True
while active:
    age = input(prompt)
    age = str(age)
    if age == 'quit':
        active = False
    else:
        if int(age) < 3:
            print("Free")
        elif int(age) >= 3 and int(age) <= 12:
            print("Your ticket price is $10")
        else:
            print("Your ticket price is $15")
        break

