import sys
import unittest

sys.path.insert(0, "/Users/sergeyvolynkin/Documents/GitHub/my-python-tasks")
import weather

class TestWeather(unittest.TestCase):
    def test_get_weather(self):
        result = weather.get_weather("spb")
        self.assertEqual(type(result), dict)
        result = weather.get_weather("msk")
        self.assertEqual(type(result), dict)
        self.assertTrue(weather.get_weather("spb"))
        self.assertTrue(weather.get_weather("msk"))


if __name__ == "__main__":
    unittest.main()