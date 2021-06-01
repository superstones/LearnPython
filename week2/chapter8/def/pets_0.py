# 关键字实参，关键字实参可以无需考虑函数调用中实参顺序，还清楚的指出函数调用中各个值的用途
def describe_pets(animal_type, pet_name):
    # 显示宠物信息
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "`s name is " + pet_name.title() + ".")


describe_pets(animal_type='dog', pet_name='rongrong')
describe_pets(animal_type='cat', pet_name='mimi')
