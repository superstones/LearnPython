from printing_functions import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)  # 切片表示法创建unprinted_designs的副本,使得函数不会修改列表本身unprinted_designs
