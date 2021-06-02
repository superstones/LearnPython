class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\nThe restaurant name is " + self.restaurant_name.title())
        print("The restaurant type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print("The number of people in this restaurant is " + str(self.number_served))

    def increment_number_served(self, number):
        self.number_served += number
        return number


my_restaurant = Restaurant('stone', 'jin')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(1)
print("I think the number of people that this restaurant may receive per day is " + str(
    my_restaurant.increment_number_served(50)))
