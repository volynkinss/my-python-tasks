import sys
import unittest

sys.path.insert(0, "/Users/sergeyvolynkin/Documents/GitHub/my-python-tasks")
import weather

class TestWeather(unittest.TestCase):
    def test_get_weather(self):
        print("\nCheck assertIsInstance_Test for the result of the get_weather function is str")
        result = weather.get_weather("spb")

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
    


                         


if __name__ == "__main__":
    unittest.main()

