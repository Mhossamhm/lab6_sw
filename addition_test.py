import unittest
from addition import add_num

class TestAdditionFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(add_num(10, 4), 14)

    def test_negative_numbers(self):
        self.assertEqual(add_num(-9, -2), -11)

    def test_float_and_integer(self):
        self.assertEqual(add_num(2.2, 2), 4.5)

    def test_zero(self):
        self.assertEqual(add_num(0, 8), 8)

    def test_large_numbers(self):
        self.assertEqual(add_num(220000, 130000), 350000)


if __name__ == '__main__':
    unittest.main()
