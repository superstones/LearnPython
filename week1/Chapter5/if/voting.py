# 简单的if语句
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
print("\n")

# if else
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
print("\n")

# if-elif-else结构
age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost if $10")
print("\n")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

# 使用多个elif代码块
age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")

# 省略else代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")
print("\n")

# 测试多个条件
requested_topping = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms")
if 'onions' in requested_topping:
    print("Adding onions")
if 'pineapple' in requested_topping:
    print("Adding pineapple")
print("\nFinished making your pizze!")

requested_topping = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_topping:# 当第一个条件通过之后，python将跳过if-elif-else结构中余下的测试
    print("Adding mushrooms")
elif 'onions' in requested_topping:
    print("Adding onions")
elif 'pineapple' in requested_topping:
    print("Adding pineapple")
print("\nFinished making your pizza!")
