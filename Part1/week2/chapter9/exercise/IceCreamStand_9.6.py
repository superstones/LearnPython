class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nThe restaurant name is " + self.restaurant_name.title())
        print("The restaurant type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        super().__init__(restaurant_name, cuisine_type)  # 继承父类的super的init的参数不需要self
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available: ")
        for flavor in self.flavors:
            print("- " + flavor.title())


my_ice_cream = IceCreamStand('stone')
my_ice_cream.flavors = ['vanilla', 'chocolate', 'black cherry']
my_ice_cream.describe_restaurant()
my_ice_cream.show_flavors()
