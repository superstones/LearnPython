# 返回简单值
def get_formatted_name(first_name, last_name):
    # 返回整洁的姓名
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')  # 调用函数时注意括号
print(musician)
