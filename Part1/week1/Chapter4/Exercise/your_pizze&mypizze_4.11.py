my_pizzas = ['chicken pizza', 'pineapple pizza', 'fruit pizza']
friend_pizza=my_pizzas[:]
my_pizzas.append('milk pizza')
friend_pizza.append('coffee pizza')
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("My friend`s favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)