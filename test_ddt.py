import unittest
import os.path
import info
from ddt import ddt, file_data


# Используем названия из geocode.json
# Проверяем, сходятся ли координаты из geocode.json с полученными только что с сайта при поиске по названию
@ddt
class Geocoding(unittest.TestCase):
    @file_data(os.path.join("geocode.json"))
    def test_coords(self, name, lat, lon, display_name):
        self.assertEqual(info.get_coords(name), (float(lat), float(lon)))

    # То же самое, но округляем координаты для менее точного сравнения (условная погрешность)
    @file_data(os.path.join("geocode.json"))
    def test_round_coords(self, name, lat, lon, display_name):
        self.assertEqual(info.get_round_coords(name), (round(float(lat), 3), round(float(lon), 3)))


# Используем координаты из main_data.json
# Проверяем, сходятся ли названия из main_data.json с полученными только что с сайта при поиске по координатам
@ddt
class RevGeocoding(unittest.TestCase):
    @file_data(os.path.join("main_data.json"))
    def test_reverse(self, display_name, lat, lon,  address):
        self.assertEqual(str(display_name), info.get_display_name(lat, lon))


if __name__ == '__main__':
    unittest.main()
