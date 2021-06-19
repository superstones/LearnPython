# 检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# 使用or检查多个条件
age_0 = 22
age_1 = 18
print((age_0 >= 21) or (age_1 >= 21)) # 为改善可读性，可将每个测试部分都分别放在一对括号内，但非必须
age_0 = 18
print((age_0 >= 21) or (age_1 >= 21))
