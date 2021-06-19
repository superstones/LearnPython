# 定义元组
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 试图修改元组的操作是被禁止的
for dimension in dimensions:
    print(dimension)

# 修改元组变量
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)

