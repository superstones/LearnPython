# 6.8宠物
pet_0 = {
    'name': 'rongrong',
    'type': 'dog',
    'owner': 'stone',
}
pet_1 = {
    'name': 'wangcai',
    'type': 'dog',
    'owner': 'Mr zhou',
}
pet_2 = {
    'name': 'xiaoqiang',
    'type': 'cat',
    'owner': 'Mr wu',
}
pets = [pet_0, pet_1, pet_2]
for pet in pets:
    print("\n Here`s what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
