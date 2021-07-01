import csv
from datetime import datetime

from matplotlib import pyplot as plt


def get_weather_data(filename, dates, rains):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                rain = float(row[19])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                rains.append(rain)


dates, rains = [], []
get_weather_data('sitka_weather_2014.csv', dates, rains)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rains, c='blue', alpha=0.5)
plt.fill_between(dates, rains, facecolor='blue', alpha=0.2)

title = "Daily rainfall amounts - 2015\nSitka, AK"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
