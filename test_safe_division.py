"""
Unit Tests for safe_division function

This module contains comprehensive unit tests to verify the behavior of safe_division,
including normal cases, edge cases, and the critical division by zero scenario.
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for the safe_division function"""
    
    def test_normal_division(self):
        """Test normal division with positive numbers"""
        result = safe_division(10, 2)
        self.assertEqual(result, 5.0)
        
    def test_negative_numerator(self):
        """Test division with negative numerator"""
        result = safe_division(-10, 2)
        self.assertEqual(result, -5.0)
        
    def test_negative_denominator(self):
        """Test division with negative denominator"""
        result = safe_division(10, -2)
        self.assertEqual(result, -5.0)
        
    def test_both_negative(self):
        """Test division with both negative numbers"""
        result = safe_division(-10, -2)
        self.assertEqual(result, 5.0)
        
    def test_float_division(self):
        """Test division with float numbers"""
        result = safe_division(7, 2)
        self.assertAlmostEqual(result, 3.5)
        
    def test_zero_numerator(self):
        """Test division with zero as numerator"""
        result = safe_division(0, 5)
        self.assertEqual(result, 0.0)
        
    def test_division_by_zero(self):
        """
        Test division by zero - Critical test case
        
        This test verifies that the safe_division function properly handles
        division by zero by returning None instead of raising ZeroDivisionError.
        This is the key safety mechanism of the function.
        """
        result = safe_division(10, 0)
        self.assertIsNone(result)
        
    def test_negative_division_by_zero(self):
        """Test division by zero with negative numerator"""
        result = safe_division(-10, 0)
        self.assertIsNone(result)
        
    def test_zero_divided_by_zero(self):
        """Test zero divided by zero edge case"""
        result = safe_division(0, 0)
        self.assertIsNone(result)
        
    def test_large_numbers(self):
        """Test division with large numbers"""
        result = safe_division(1000000, 1000)
        self.assertEqual(result, 1000.0)
        
    def test_small_numbers(self):
        """Test division with very small numbers"""
        result = safe_division(0.001, 0.1)
        self.assertAlmostEqual(result, 0.01)


if __name__ == '__main__':
    unittest.main()
