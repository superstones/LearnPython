import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()
    # 设置绘图窗口的尺寸
    # plt.figure(dpi=300, figsize=(10, 6))
    # 隐藏坐标轴
    current_axes = plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False)
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    points_number = list(range(rw.number_points))
    # plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # plt.scatter(rw.x_values, rw.y_values, c=points_number,
    #             cmap=plt.cm.Blues, edgecolors='none', s=1)
    plt.plot(rw.x_values, rw.y_values,linewidth=2)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
