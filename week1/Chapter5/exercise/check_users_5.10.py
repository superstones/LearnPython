# 5.10检查用户名
current_users = ['admin', 'stone', 'chr', 'Mr wu', 'bingbingwang' ,'JOHN']
new_users =['stone', 'john', 'lucy', 'paul', 'tony']

#将current_users中大写元素全部转换为小写
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user in current_users_lower:
        print(new_user + " is used, you should enter another username.")
    else:
        print(new_user + " is not used.")
