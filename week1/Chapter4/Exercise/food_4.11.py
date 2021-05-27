my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food=my_foods[:]
my_foods.append('ice cream')
friend_food.append('hamburger')
for food in my_foods:
    print(food)
print("\n")
for food_friend in friend_food:
    print(food_friend)