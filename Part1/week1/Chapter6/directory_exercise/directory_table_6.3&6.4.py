# 6.3词汇表
directory = {
    'print': 'Output statement',
    'min': 'Find the smallest number in the list',
    'max': 'Find the largest number in the list',
    'sum': 'Sum the list',
    'pop': 'Delete the list of element',
    'for': 'Repeat statement',
    '+': 'Add two objects',
    '-': 'Get a negative number or subtract one number from another',
    '*': 'Multiply two numbers or return a string repeated several times',
    '%': 'Returns the remainder of the division',
}
print("print: " + directory['print'])
print("min: " + directory['min'])
print("max: " + directory['max'])
print("sum: " + directory['sum'])
print("pop: " + directory['pop'])
print("\n")

# 6.5词汇表2
for word, means in directory.items():
    print(word + ":" + means)
