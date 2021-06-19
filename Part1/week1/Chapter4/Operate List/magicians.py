#使用循环遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + ", that was a great trick")
    print("I can`t wait to see your next trick, " + magician.title() + ".\n")

print("Thank you everyone. That was a great magic show!")#在for循环后面，没有缩进的代码只执行一次


