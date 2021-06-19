# 结合位置实参和任意数量实参,任意数量实参的形参必须放在最后
def make_pizza(size, *toppings):
    # 概述要制作的pizza
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'mushrooms')
make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')
