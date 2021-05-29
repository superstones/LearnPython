# 修改字典中的值，移动外星人
alien_0 = {'x_position': 0, 'y_position': 25 , 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# alien_0['speed'] = 'fast'
# 向右移动外星人
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# 删除键-值对
alien_1 = {'color': 'green', 'points': 5}
print(alien_1)
del alien_1['points']
print(alien_1)
