import json


def get_stored_number():
    """如果存储了用户喜欢的数字，就获取它"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def get_new_number():
    favorite_number = input("What is your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number


def show_favorite_number():
    favorite_number = get_stored_number()
    if favorite_number:
        print("I know your favorite number!It`s " + favorite_number)
    else:
        favorite_number = get_new_number()
        print("I know your favorite number!It`s " + favorite_number)

show_favorite_number()
