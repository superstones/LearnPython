prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break # 任何Python循环中都可使用break语句。
    else:
        print("I`d love to go to " + city.title() + "!")
