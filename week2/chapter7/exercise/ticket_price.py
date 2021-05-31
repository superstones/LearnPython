# 7.5电影票
prompt = "How old are you? Please enter your age. "
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("free")
    elif age >= 3 and age <= 12:
        print("Your ticket price is $10")
    else:
        print("Your ticket price is $15")
