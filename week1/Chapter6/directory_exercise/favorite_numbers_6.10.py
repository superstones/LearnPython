# 喜欢的数字
favorite_numbers = {
    'Stone': [9, 8, 6],
    'Bing': [6, 2],
    'Wu': [8, 6],
    'Yue': [2, 8],
    'Cheng': [6, 9, 8],
}
for name, numbers in favorite_numbers.items():
    print(name + "`s favorite numbers are:")
    for number in numbers:
        print(str(number))
