# 6.9喜欢的地方
favorite_places = {
    'stone': ['Paris', 'chengdu', 'hainan'],
    'Mr wu': ['Xi`an', 'hainan'],
    'Mr wang': ['Xi`an']
}
for name, places in favorite_places.items():
    if len(places) == 1:
        print(name.title() + "`s favorite place is:")
    else:
        print(name.title() + "`s favorite places are:")
    for place in places:
        print("\t" + place.title())
