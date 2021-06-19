def cars_info(manufacturers, models, **car_info):
    # 将车辆信息存储到字典中
    profile = {}
    profile['manufacturer'] = manufacturers
    profile['model'] = models
    for key, value in car_info.items():
        profile[key] = value
    return profile


car = cars_info('Volkswagen', 'Audi Q5L', color='blue', tow_package=True)
print(car)
