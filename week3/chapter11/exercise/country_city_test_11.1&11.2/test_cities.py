# 11.1&11.2城市和国家，人口数量
import unittest
from city_functions import get_city_country_name


class Cities(unittest.TestCase):

    def test_city_country(self):
        full_name = get_city_country_name('santiago', 'chile')
        self.assertEqual(full_name, 'Santiago Chile')

    def test_city_country_population(self):
        full_name = get_city_country_name('santiago', 'chile', '5000000')
        self.assertEqual(full_name, 'Santiago Chile-5000000')


if __name__ == '__main__':
    unittest.main
