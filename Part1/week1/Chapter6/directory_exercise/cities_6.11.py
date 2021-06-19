cities = {
    'paris': {
        'country': 'france',
        'population': '2.14 million',
        'fact': 'City of romance'

    },
    'chengdu': {
        'country': 'china',
        'population': '20.938 million',
        'fact': 'Dujiangyan'

    },
    'sanya': {
        'country': 'china',
        'population': '669,300',
        'fact': 'City of romance'
    },
}
for city, city_info in cities.items():
    print("\nCity:" + city)
    population = city_info['population']
    fact = city_info['fact']
    print("population:" + str(population))
    print("fact: " + fact)
