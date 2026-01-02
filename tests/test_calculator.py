import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 1), 2)

    def test_divide_by_zero(self):
        # This test expects a ValueError, but the code raises ZeroDivisionError (or crashes)
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

if __name__ == "__main__":
    unittest.main()
