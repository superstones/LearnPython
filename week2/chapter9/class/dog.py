# 创建Dog类

class Dog():

    def __init__(self, name, age):  # __init__()方法是一个特殊的方法，每次根据Dog类创建新实例时，python都会自动运行它。
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


# 根据类创建实例
my_dog = Dog('Rongrong', 11)
your_dog = Dog('lucy', 3)
my_dog.sit()
my_dog.roll_over()
print("My dog`s name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")


print("\nYour dog`s name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()
