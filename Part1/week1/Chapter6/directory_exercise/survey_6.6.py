favorite_language = {
    'stone': 'python',
    'john': 'java',
    'tony': 'c',
    'phil': 'python',
}
peoples = ['stone', 'john', 'tony', 'jack', 'Mr wu']
for people in peoples:  # 先遍历出来people名单再与已接受调查的人进行比较
    if people in favorite_language.keys():
        print("\n" + people.title() + ", thank you for taking the poll.")
    else:
        print("\n" + people.title() + ", what`s your favorite programming language?")
