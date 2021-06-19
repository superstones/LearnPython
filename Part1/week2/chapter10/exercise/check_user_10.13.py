import json


# def greet_user():
#     """问候用户，并指出其名字"""
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w')as f:
#             json.dump(username, f)
#             print("We`ll remember you when you come back, " + username + "!")
#     else:
#         print("Welcome back, " + username + "!")
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w')as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        correct = input("Are you " + username + "? (y/n)")
        if correct == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We`ll remember you when you come back, " + username + "!")


greet_user()