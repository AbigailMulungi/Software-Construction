import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """A class to test the functionality of the Calculator class."""

    def setUp(self):
        """Set up a Calculator instance before each test."""
        self.calculator = Calculator()

    def test_summation(self):
        """Test the addition method of the Calculator."""
        result = self.calculator.sum(3, 5)
        self.assertEqual(result, 8)

    def test_difference(self):
        """Test the subtraction method of the Calculator."""
        result = self.calculator.difference(10, 3)
        self.assertEqual(result, 7)

    def test_product(self):
        """Test the multiplication method of the Calculator."""
        result = self.calculator.product(4, 6)
        self.assertEqual(result, 24)

    def test_quotient(self):
        """Test the division method of the Calculator."""
        result = self.calculator.quotient(15, 3)
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        """Test division by zero handling in the Calculator."""
        with self.assertRaises(ValueError):
            self.calculator.quotient(10, 0)

if __name__ == '__main__':
    unittest.main()
