import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期和最高气温和最低气温
filename = 'death_valley_2014.csv'


def get_weather_data(filename, dates, highs, lows):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, column_header in enumerate(header_row):
            print(index, column_header)

        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


dates, highs, lows = [], [], []
get_weather_data('sitka_weather_2014.csv', dates, highs, lows)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

dates, highs, lows = [], [], []
get_weather_data('death_valley_2014.csv', dates, highs, lows)
# 设置图片的格式

plt.plot(dates, highs, c='red', alpha=0.3)
plt.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

title = "Daily high and low temperatures - 2014\nSitka, AK and Death Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.xlabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
