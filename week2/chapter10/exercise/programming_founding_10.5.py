# 关于编程的调查
file_name = "Reasons.txt"
prompt = "\nWhy do you like programming? "
prompt += "\nEnter 'q' to quit. "
while True:
    reason = input(prompt)
    if str(reason) == 'q':
        break
    else:
        with open(file_name, 'a') as f:
            f.write(reason + "\n")
