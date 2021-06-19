# one simple directory
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 访问字典中的值
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 添加键-值对
alien_1 = {'color': 'green', 'points': 5}
print(alien_1)
alien_1['x_position'] = 0
alien_1['y_position'] = 25
print(alien_1)

# 创建一个空字典
alien_2 = {}
alien_2['color'] = 'green'
alien_2['points'] = 5
print(alien_2)

# 修改字典中的值
alien_3 = {'color': 'green', 'points': 5}
print("The aline is " + alien_3['color'] + ".")
alien_3['color'] = 'yellow'
print("The aline now is " + alien_3['color'] + ".")