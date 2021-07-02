import json
import pygal
import math

# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))
    print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))

dates = []
months = []
weeks = []
weekdays = []
close = []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# line_chart.title = '收盘价(￥)'
# line_chart.x_labels = dates
# N = 20  # x坐标轴每隔20显示一次
# line_chart.x_labels_major = dates[::N]
# line_chart.add('收盘价', close)
# line_chart.render_to_file('收盘价折线图(￥) .svg')

# 时间序列特征初探
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数转换(￥)'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变换折线图(￥) .svg')

with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in ['收盘价周日均值.svg', '收盘价对数变换折线图(￥) .svg', '收盘价折线图(￥) .svg',
                '收盘价星期均值(￥) .svg', '收盘价星期均值.svg', '收盘价月日均值.svg']:
        html_file.write('<object type = "image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
    html_file.write('</body></html>')

