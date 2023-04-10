import sys

sys.path.insert(0, "/Users/ludocka/Desktop/IlyaTeachMe/my-python-tasks")
import Ex2
import unittest


class TestEx2(unittest.TestCase):
    def test_get_elements_from_input(self):
        result = sum(Ex2.get_elements_from_input(1))
        self.assertEqual(result, 12)


if __name__ == "__main__":
    unittest.main()
