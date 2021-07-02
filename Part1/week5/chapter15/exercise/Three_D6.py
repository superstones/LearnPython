import pygal
from die import Die

die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# 投掷多次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

x_labels = []
for x_label in results:
    if x_label not in x_labels:
        x_labels.append(x_label)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling three D6 1000 times."
hist.x_labels = sorted(x_labels)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)

hist.render_to_file('Three D6.svg')
