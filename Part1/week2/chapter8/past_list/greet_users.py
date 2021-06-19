# 向函数传递列表
def greet_users(names):
    for name in names:
        message = "Hello, " + name.title() + "!"
        print(message)


usernames = ['stone', 'bingbingwang', 'Mr wu']
greet_users(usernames)
