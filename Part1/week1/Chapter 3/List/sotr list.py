#使用sort方法对列表元素进行排序(对列表排列顺序的修改是永久的)
cars=['bmw', 'audi', 'toyota', 'subaru']
cars.sort()#按字母顺序排序
print(cars)

cars.sort(reverse=True)#按与字母顺序相反进行排序
print(cars)

#使用sorted方法对列表元素进行临时排序
cars=['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the sorted list:")
print(sorted(cars,reverse=True))

print("\nHere is the original list again:")
print(cars)

#使用reverse方法反转列表元素的排列顺序(这种修改是永久性的)
cars=['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

car="Rolls Royce"
print("\n"+car) #当变量存储为列表时无法对其进行拼接

#确定列表的长度
cars=['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))


