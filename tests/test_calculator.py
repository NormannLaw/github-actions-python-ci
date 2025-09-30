import unittest
from src.calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 7), -2)
        self.assertEqual(subtract(14, 3), 11)
        self.assertEqual(subtract(0, -2), 2)

    def test_divide(self):
        self.assertEqual(divide(1, 2), 0.5)
        self.assertEqual(divide(0, 7), 0)
        self.assertEqual(divide(-15, 3), -5)

if __name__ == '__main__':
   unittest.main()