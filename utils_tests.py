from utils import *
import unittest

# Framework from https://docs.python.org/3/library/unittest.html
class TestMethods(unittest.TestCase):
    def test_reversed_int(self):
        self.assertEqual(utils.reversed(123456), 654321)
    def test_reversed_string(self):
        self.assertEqual(utils.reversed("1248"), 8421)
    def test_reversed_float(self):
        with self.assertRaises(ValueError):
            utils.reversed(123.456)

    def test_formatter_int(self):
        self.assertEqual(utils.formatter(12), [1100, 14])
    def test_formatter_string(self):
        self.assertEqual(utils.formatter(14), [1110, 16])
    def test_formatter_float(self):
        with self.assertRaises(ValueError):
            utils.formatter(1.2)

if __name__ == '__main__':
    unittest.main()

