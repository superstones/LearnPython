# 10.10常见单词

def count_words(file_name):
    try:
        with open(file_name, 'r', encoding='UTF-8') as f:
            f_read = f.read()
            contents = f_read.lower().split()
    except FileNotFoundError:
        pass
        # msg = "Sorry, the file " + file_name + " does not exist."
        # print(msg)
    else:
        num_words = contents.count('love')
    print("The file " + file_name + " has about " + str(num_words) + " words.")


file_names = ['Alice’s Adventures in Wonderland.txt', 'Mary Wollstonecraft (Godwin) Shelley.txt',
              'Pride and Prejudice.txt', 'The Great Gatsby.txt']
for file_name in file_names:
    count_words(file_name)
