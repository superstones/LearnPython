# 7.4披萨配料
prompt = "\nPlease enter a series of pizza ingredients:"
prompt += "\nEnter 'quit' to end the program. "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("Adding " + topping)
