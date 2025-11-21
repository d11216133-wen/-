"""
Unit Tests using the UNSAFE version of safe_division

This test file demonstrates what happens when the division by zero
handling is removed from the safe_division function.
"""

import unittest
from safe_division_unsafe import safe_division


class TestUnsafeDivision(unittest.TestCase):
    """Test cases using the unsafe version - will FAIL for division by zero"""
    
    def test_normal_division(self):
        """Test normal division with positive numbers"""
        result = safe_division(10, 2)
        self.assertEqual(result, 5.0)
        
    def test_division_by_zero(self):
        """
        Test division by zero - This will FAIL
        
        Expected: function returns None
        Actual: function raises ZeroDivisionError
        """
        result = safe_division(10, 0)
        self.assertIsNone(result)
        
    def test_negative_division_by_zero(self):
        """Test division by zero with negative numerator - This will FAIL"""
        result = safe_division(-10, 0)
        self.assertIsNone(result)
        
    def test_zero_divided_by_zero(self):
        """Test zero divided by zero - This will FAIL"""
        result = safe_division(0, 0)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
