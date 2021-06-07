# 8.5描述城市
def describe_city(name, country='france'):
    print(name.title() + " is in " + country.title())


describe_city('Paris')
describe_city('Provence')
describe_city('Montpellier')
describe_city('Hawaii State', country='american')
