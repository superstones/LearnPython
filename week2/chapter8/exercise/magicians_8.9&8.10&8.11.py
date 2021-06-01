# 8.9&8.10&8.11
def show_magicians(names):
    for name in names:
        print(name)


def make_great(names):
    great_magicians = []
    while names:
        magician = names.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        names.append(great_magician)
    return names


magicians_name = ['Harry Houdini', 'David Copperfield', 'Criss Angel']
show_magicians(magicians_name)

print("\n")
great_magicians = make_great(magicians_name[:])
show_magicians(great_magicians)

print("\nOriginal magicians: ")
show_magicians(magicians_name)
