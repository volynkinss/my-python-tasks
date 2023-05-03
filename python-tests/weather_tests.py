import sys
import unittest

sys.path.insert(0, "/Users/sergeyvolynkin/Documents/GitHub/my-python-tasks")
import weather

class TestWeather(unittest.TestCase):
    def test_get_weather(self):
        print("\nCheck assertIsInstance_Test for the result of the get_weather function is str")
        result = weather.get_weather("spb")
        result = weather.get_weather("msk")
        result = weather.get_weather("muc")
        self.assertIsInstance(result, str)

    def test_get_weather_errors(self):
        print("\nCheck assertRaises_Test for get_weather function errors")
        with self.assertRaises(NameError):
            weather.get_weather(fadf)
        with self.assertRaises(KeyError):
            weather.get_weather("fadf")
        with self.assertRaises(AttributeError):
            weather.get_weather(1)
        with self.assertRaises(TypeError):
            weather.get_weather()
    
    def test_list_of_cities(self):
        print("\nCheck assertIsInstance_Test for list_of_cities is a dictionary")
        self.assertIsInstance(weather.list_of_cities, dict)
    
    def test_Class_City(self):
        print("\nCheck test_Class_City for correspondence with the dictionary list_of_cities meaning")
        request_city_spb = weather.list_of_cities["spb"]
        self.assertEqual(request_city_spb.name , "Saint Petersburg")
        self.assertEqual(request_city_spb.latitude, 59.94)
        self.assertEqual(request_city_spb.longitude, 30.31)

        request_city_msk = weather.list_of_cities["msk"]
        self.assertEqual(request_city_msk.name , "Moscow")
        self.assertEqual(request_city_msk.latitude, 55.75)
        self.assertEqual(request_city_msk.longitude, 37.62)

        request_city_muc = weather.list_of_cities["muc"]
        self.assertEqual(request_city_muc.name , "Munich")
        self.assertEqual(request_city_muc.latitude, 48.14)
        self.assertEqual(request_city_muc.longitude, 11.58)

                         


if __name__ == "__main__":
    unittest.main()

