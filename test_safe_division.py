import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for the safe_division function."""
    
    def test_normal_division(self):
        """Test normal division with non-zero divisor."""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(9, 3), 3.0)
        self.assertEqual(safe_division(7, 2), 3.5)
    
    def test_division_by_zero(self):
        """Test that division by zero returns None."""
        self.assertIsNone(safe_division(10, 0))
        self.assertIsNone(safe_division(0, 0))
        self.assertIsNone(safe_division(-5, 0))
    
    def test_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_zero_dividend(self):
        """Test division with zero as dividend."""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(0, -3), 0.0)
    
    def test_float_numbers(self):
        """Test division with floating point numbers."""
        self.assertAlmostEqual(safe_division(5.5, 2.0), 2.75)
        self.assertAlmostEqual(safe_division(1.0, 3.0), 0.3333333333333333)
    
    def test_large_numbers(self):
        """Test division with large numbers."""
        self.assertEqual(safe_division(1000000, 1000), 1000.0)
        self.assertAlmostEqual(safe_division(999999, 3), 333333.0)


if __name__ == '__main__':
    unittest.main()
