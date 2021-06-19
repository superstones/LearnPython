# 10.6加法运算
print("\nAddition calculation")
print("Please enter two numbers.")
try:
    number_1 = input("Please enter number1: ")
    number_2 = input("Please enter number2: ")
    add_number = int(number_1) + int(number_2)
except ValueError:
    print("Please key in numbers.")
else:
    print("计算结果为: " + str(add_number))
