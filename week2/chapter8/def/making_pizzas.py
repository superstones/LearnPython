# 将函数存储在模块中并调用
import pizza_model

pizza_model.make_pizza(16, 'mushrooms')
pizza_model.make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')

from pizza_model import make_pizza

make_pizza(16, 'mushrooms')
make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')

from pizza_model import make_pizza as mp

mp(16, 'mushrooms')
mp(12, 'pepperoni', 'green peppers', 'extra cheese')

import pizza_model as pm

pm.make_pizza(16, 'mushrooms')
pm.make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')

from pizza_model import *

make_pizza(16, 'mushrooms')
make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')
