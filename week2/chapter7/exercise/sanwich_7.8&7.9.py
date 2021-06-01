# 7.8熟食店&7.9五香烟熏牛肉
sandwich_orders = ['chicken', 'ham', 'cabbage', 'beef', 'pastrami',
                   'pastrami', 'pastrami']
finished_sandwiches = []

print("Pastrami sandwiches sold out")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_order)
    print("I made your " + sandwich_order + "sandwich")
print("The following finished sandwiches are: ")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche + " sandwich")
