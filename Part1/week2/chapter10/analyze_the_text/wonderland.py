# 分析文本
# title = "Alice in Wonderland"
# print(title.split())
def count_words(file_name):
    # 计算一个文件大致包含多少个单词
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass  # pass语句可以在异常发生时，不进行任何提示
        # msg = "Sorry, the file " + file_name + "does not exist."
        # print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " + str(num_words) + " words.")


# file_name = 'alice.txt'
# count_words(file_name)
file_names = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
for file_name in file_names:
    count_words(file_name)
