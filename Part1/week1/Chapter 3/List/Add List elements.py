motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0]="stone"
print(motorcycles)
motorcycles.append("ducati")#在列表末尾添加元素
print(motorcycles)

motorcycles=[] #创建一个空列表并添加元素
motorcycles.append("yamaha")
motorcycles.append("suzuki")
motorcycles.append("honda")
print(motorcycles)

motorcycles=["suzuki", "honda", "yamaha"]
motorcycles.insert(0,"ducati") #在索引0出添加空间并将ducati存储到这个地方
print(motorcycles)