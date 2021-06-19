#函数range的使用
for value in range(1, 5):
    print(value)
print("\n")
for value in range(1, 6):
    print(value)

#使用range创建数字列表
numbers = list(range(1, 6))
print(numbers)

#创建偶数列表
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#创建平方数列表
squares = []
for value in range(1,11):
    sqare = value**2
    squares.append(sqare)
print(squares)

#使用临时变量会让代码更易读，在其他情况下，会使代码无谓地变长
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#对数字列表进行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#列表解析
squares = [value**2 for value in range(1,11)]
print(squares)
