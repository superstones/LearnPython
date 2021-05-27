#4.5计算一百万的总和
numbers = [number for number in range(1,1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print("\n")

#4.6奇数
numbers = [number for number in range(1,21,2)]
for value in numbers:
    print(value)
print("\n")

#4.7 3的倍数
numbers = [number for number in range(3,31,3)]
for value in numbers:
    print(value)
print("\n")

#4.9 立方
cubes = []
for cube in range(1,11):
    cubes.append(cube**3)
for value in cubes:
    print(value)