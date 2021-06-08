from collections import OrderedDict

directory = OrderedDict()

directory['print'] = 'Output statement'
directory['min'] = 'Find the smallest number in the list'
directory['max'] = 'Find the largest number in the list'
directory['sum'] = 'Sum the list'
directory['pop'] = 'Delete the list of element'
directory['for'] = 'Repeat statement'
directory['+'] = 'Add two objects'
directory['-'] = 'Get a negative number or subtract one number from another'
directory['*'] = 'Multiply two numbers or return a string repeated several times'
directory['%'] = 'Returns the remainder of the division'

for name, value in directory.items():
    print(name + ": " + value)
