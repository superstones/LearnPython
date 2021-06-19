cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())
print(cars[0] == 'bmw')

# 将变量的值转换为小写，再进行比较
car = 'Audi'
print(car.lower() == 'audi')
print(car)
