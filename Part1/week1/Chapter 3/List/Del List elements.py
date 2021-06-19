#del
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[0] #删除列表中元素  del可以删除任何位置处的列表元素，前提是知道其索引,删除以后就无法再进行访问
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#pop
#pop可删除列表末尾的元素，相当于弹出栈顶元素，如果后续还需要使用元素，则使用pop方法
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")


motorcycles = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles.pop(0)#弹出列表中第一个元素并保存到first_owned中
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#remove
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.remove("suzuki")#根据值删除元素，只能删除第一个指定的值，如果有多个相同的值需要使用循环来判断并进行删除
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
too_expensive="suzuki"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + "is too expensive for me.")

