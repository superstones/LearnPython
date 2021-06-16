# 10.7加法计算器

while True:
    print("\nAddition calculation")
    print("Please enter two numbers.")
    print("(Enter 'q' to quit at any time.)")
    try:
        number_1 = input("Please enter number1: ")
        if number_1 == 'q':
            break
        number_2 = input("Please enter number2: ")
        if number_2 == 'q':
            break
        add_number = int(number_1) + int(number_2)
    except ValueError:
        print("Please key in numbers.")
    else:
        print("计算结果为: " + str(add_number))
