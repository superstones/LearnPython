#切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])#若没有指定第一个索引，python将自动从列表开头开始。
print(players[2:])#将提取第3个元素到末尾
print(players[-3:])#无论列表多长都将提取末尾的最后三个元素

#遍历切片
print("Here are thr first three players on my team.")
for player in players[:3]:
    print(player.title())

#复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food=my_foods[:]
my_foods.append('ice cream')
friend_food.append('hamburger')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend`s favorite foods are:")
print(friend_food)
