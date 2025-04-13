import unittest
from math_utils import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(0, 1), 1)

if __name__ == '__main__':
    unittest.main()