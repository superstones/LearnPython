dream_places = {}
polling_active = True
while polling_active:
    name = input("What is your name? ")
    dream_place = input("If you could visit one place in the world, where would you go? ")
    dream_places[name] = dream_place
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, dream_place in dream_places.items():
    print(name.title() + " would like to visit " + dream_place.title())
