# 三明治
def make_sandwich(*toppings):
    # 概述所要制作的三明治
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_sandwich('chicken')
make_sandwich('ham', 'vegetables')
make_sandwich('chicken', 'ham', 'vegetables')
