# 检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# 检查特定值是否包含在列表中
requested_topping = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_topping)
print('pepperoni' in requested_topping)

# 检查特定值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
