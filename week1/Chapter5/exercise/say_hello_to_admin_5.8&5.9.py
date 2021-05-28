# 5.8以特殊方式跟管理员打招呼 &5.9处理没有用户的情形
# users = ['stone', 'admin', 'bingbingwang', 'chr', 'Mr wu']
users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + " ,thank you for logging in again.")
else:
    print("We need to find some users")