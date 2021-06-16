import json

filename = 'favorite_number.json'

with open(filename, 'w') as f:
    favorite_number = input("What is your favorite number? ")
    json.dump(favorite_number, f)

with open(filename) as f:
    favorite_number = json.load(f)
    print("I know your favorite number!It`s " + favorite_number)
