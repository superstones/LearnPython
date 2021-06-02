# 9.1&9.2餐馆&三家餐馆
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nThe restaurant name is " + self.restaurant_name.title())
        print("The restaurant type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")


restaurant = Restaurant('sufuji', 'sichuan')
restaurant.describe_restaurant()
restaurant.open_restaurant()
my_restaurant = Restaurant('stone', 'jin')
my_restaurant.describe_restaurant()
your_restaurant = Restaurant('wu', 'jin')
your_restaurant.describe_restaurant()
chr_restaurant = Restaurant('chr', 'jin')
chr_restaurant.describe_restaurant()
