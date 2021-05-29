favorite_language = {
    'stone': 'python',
    'john': 'java',
    'tony': 'c',
    'phil': 'python',
}
print("Stone`s favorite language is " + favorite_language['stone'].title() + ".")

# 遍历字典
for name, language in favorite_language.items():
    print(name.title() + "`s favorite language is " + language.title() + ".")

# 遍历字典中的所有键
for name in favorite_language.keys():
    print(name.title())
for name in favorite_language:  # 可以不加key()方法，遍历字典时会默认遍历所有的键，加上可以让代码更易于理解
    print(name.upper())

friends = ['phil', 'tony']
for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              " , I see your favorite language is " + favorite_language[name].title() + "!")
if 'erin' not in favorite_language.keys():
    print("\nErin, please take our poll!")

# 按顺序遍历字典中的所有键
for name in sorted(favorite_language.keys()):
    print("\n" + name.title() + ", thank you for taking the poll.")

# 遍历字典中所有的值
print("The following languages have been mentioned:")
for language in favorite_language.values():
    print(language.title())
print("\n")

# 使用set()剔除重复项
print("The following languages have been mentioned:")
for language in set(favorite_language.values()):
    print(language.title())