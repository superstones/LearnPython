# 默认值 使用时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参。
def describe_pets(pet_name, animal_type='dog'):
    # 显示宠物信息
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "`s name is " + pet_name.title() + ".")


describe_pets(pet_name='rongrong')
describe_pets(pet_name='mimi', animal_type='cat')


