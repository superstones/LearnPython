# 位置实参
def describe_pets(animal_type, pet_name):
    # 显示宠物信息
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "`s name is " + pet_name.title() + ".")


describe_pets('dog', 'rongrong')
describe_pets('cat', 'mimi')

# 调用函数中实参的顺序与函数定义中形参的顺序需要一致
