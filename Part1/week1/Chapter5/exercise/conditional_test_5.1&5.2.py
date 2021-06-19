# 5.1条件测试
country = 'Paris'
print("Is country == 'Paris'?,I predict True.")
print(country == 'Paris')

print("\nIs country == 'Beijing'?,I predict False.")
print(country == 'Beijing')

animal = 'dog'
print("\nIs animal == 'dog?,I predict True.")
print(animal == 'dog')
print("\nIs animal == 'cat'?,I predict False.")
print(animal == 'cat')

name = 'chr'
print("\nIs name == 'chr'?,I predict True.")
print(name == 'chr')
print("\nIs name == 'stone'?,I predict False.")
print(name == 'stone')

number = 65
print("\nIs number == '65'?,I predict Ture.")
print(number == 65)
print("\nIs number =='60'?,I predict False.")
print(number == 60)

car = 'audi'
print("\nIs car == 'audi'?,I predict True.")
print(car == 'audi')
print("\nIs car == 'toyota'?,I predict False.")
print(car == 'toyota')

#5.2 更多的条件测试
a1 = 'morning'
a2 = 'afternoon'
a3 = 'morning'
country = ['China', 'Paris', 'Nanjing', 'Chengdu', 'Hainan']
# 检查两个字符串相等和不相等
if a1 == a3:
    print("a1 equal a3")
if a1 == a2:
    print("a1 not equal a2")
print("\n")

# 使用函数lower()的测试
b1 = "Animal"
if b1.lower() == 'animal':
    print("True")
if b1 != 'animal':
    print("False")
print("\n")

# 检查两个数字相等、不等、大于、小于、大于等于和小于等于
number_1 = 18
number_2 = 18
if number_1 == number_2:
    print("True")
number_2 = 23
if number_1 != number_2:
    print("False")
number_2 = 20
if number_2 > number_1:
    print("True")
if number_1 < number_2:
    print("False")
if number_1 >= 18:
    print("True")
if number_2 <=20:
    print("False")
print("\n")

# 使用关键字and和or的测试
if number_1 == 18 and number_2 == 20:
    print("True")
if number_1 == 18 or number_2 == 18:
    print("False")
print("\n")

# 测试特定的值是否包含在列表中
if 'China' in country:
    print("True")
if 'France' not in country:
    print("False")






