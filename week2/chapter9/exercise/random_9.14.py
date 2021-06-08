from random import *


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, times):
        self.times = times
        for x in range(times):
            x = randint(1, self.sides)
            print(x)


my_die = Die()
my_die.roll_die(10)
print("\n")
ten_die = Die(10)
ten_die.roll_die(10)
print("\n")
twenty_die = Die(20)
twenty_die.roll_die(10)
