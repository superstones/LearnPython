# 存储所点pizza的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# 概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza" + " with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_language = {
    'stone': ['python', 'ruby'],
    'john': ['java', 'c'],
    'tony': ['c'],
    'phil': ['python', 'haskell'],
}
for name, langeuages in favorite_language.items():
    if len(langeuages) == 1:
        print("\n" + name.title() + "`s favorite language is:")
    else:
        print("\n" + name.title() + "`s favorite language are:")
    for language in langeuages:
        print("\t" + language.title())
