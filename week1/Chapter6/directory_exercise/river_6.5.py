# 6.5河流
three_river = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'the Yangtze River': 'china',
}
for river, country in three_river.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
print("\n")
for river in three_river.keys():
    print("The river is " + river.title() + ".")
print("\n")
for country in three_river.values():
    print(country.title())


