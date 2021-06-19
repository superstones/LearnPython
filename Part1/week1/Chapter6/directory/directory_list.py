# 将字典放到列表中
aliens_0 = {'color': 'green', 'points': 5}
aliens_1 = {'color': 'yellow', 'points': 10}
aliens_2 = {'color': 'red', 'points': 15}
aliens = [aliens_0, aliens_1, aliens_2]
for alien in aliens:
    print(alien)

# 使用range()生成30个外星人
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

# 显示创建了多少外星人
print("Total number of aliens:" + str(len(aliens)))

# 将前三个外星人修改为黄色的，速度为中等且值10个点
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'

# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
