import matplotlib.pyplot as plt
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

# x_value = [1, 2, 3, 4, 5]
# y_value = [1, 4, 9, 16, 25]
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置图表标题并给坐标轴上加上标签
plt.title("Square Numbers ", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
# # 设置刻度标记的大小
plt.tick_params(axis="both", which='major', labelsize=14)

plt.savefig('squares_plot.png', bbox_inches='tight')

