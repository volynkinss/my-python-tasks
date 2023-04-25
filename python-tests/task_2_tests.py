import sys
import unittest

sys.path.insert(0, "/Users/ludocka/Desktop/IlyaTeachMe/my-python-tasks")
import Ex2


class TestEx2(unittest.TestCase):
    def test_get_array(self):
        self.assertEqual(Ex2.get_array(1, 4, 5, 2, 0), 12)

    def test_get_array_with_error(self):
        with self.assertRaises(NameError):
            Ex2.get_array(B)


if __name__ == "__main__":
    unittest.main()
