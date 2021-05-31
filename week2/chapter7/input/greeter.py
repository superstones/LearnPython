name = input("Please enter your name: ")
print("Hello, " + name + "!")

# 提示超过两行，可将提示先存储到一个变量中
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name)

