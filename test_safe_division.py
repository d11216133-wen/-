"""
Unit tests for the safe_division function.
This test suite covers normal operations, edge cases, and error handling.
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for the safe_division function."""
    
    def test_normal_division_positive_integers(self):
        """Test division of two positive integers."""
        result = safe_division(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_normal_division_negative_integers(self):
        """Test division with negative integers."""
        result = safe_division(-10, 2)
        self.assertEqual(result, -5.0)
        
        result = safe_division(10, -2)
        self.assertEqual(result, -5.0)
        
        result = safe_division(-10, -2)
        self.assertEqual(result, 5.0)
    
    def test_division_with_floats(self):
        """Test division with floating point numbers."""
        result = safe_division(10.5, 2.5)
        self.assertAlmostEqual(result, 4.2, places=7)
        
        result = safe_division(7.0, 2.0)
        self.assertEqual(result, 3.5)
    
    def test_division_by_zero(self):
        """Test that division by zero returns None."""
        result = safe_division(10, 0)
        self.assertIsNone(result)
        
        result = safe_division(0, 0)
        self.assertIsNone(result)
        
        result = safe_division(-5, 0)
        self.assertIsNone(result)
    
    def test_zero_dividend(self):
        """Test division when dividend is zero (but divisor is not)."""
        result = safe_division(0, 5)
        self.assertEqual(result, 0.0)
        
        result = safe_division(0, -3)
        self.assertEqual(result, 0.0)
    
    def test_fractional_results(self):
        """Test division that results in fractions."""
        result = safe_division(1, 3)
        self.assertAlmostEqual(result, 1/3, places=7)
        
        result = safe_division(7, 3)
        self.assertAlmostEqual(result, 7/3, places=7)
    
    def test_very_small_divisor(self):
        """Test division with very small divisor (but not zero)."""
        result = safe_division(1, 0.0001)
        self.assertEqual(result, 10000.0)
    
    def test_very_large_numbers(self):
        """Test division with very large numbers."""
        result = safe_division(1000000, 1000)
        self.assertEqual(result, 1000.0)
        
        result = safe_division(1e10, 1e5)
        self.assertEqual(result, 1e5)
    
    def test_type_error_with_string(self):
        """Test that TypeError is raised when string is passed."""
        with self.assertRaises(TypeError):
            safe_division("10", 2)
        
        with self.assertRaises(TypeError):
            safe_division(10, "2")
        
        with self.assertRaises(TypeError):
            safe_division("10", "2")
    
    def test_type_error_with_none(self):
        """Test that TypeError is raised when None is passed."""
        with self.assertRaises(TypeError):
            safe_division(None, 2)
        
        with self.assertRaises(TypeError):
            safe_division(10, None)
    
    def test_type_error_with_list(self):
        """Test that TypeError is raised when list is passed."""
        with self.assertRaises(TypeError):
            safe_division([10], 2)
        
        with self.assertRaises(TypeError):
            safe_division(10, [2])
    
    def test_mixed_int_float_types(self):
        """Test division with mixed int and float types."""
        result = safe_division(10, 2.0)
        self.assertEqual(result, 5.0)
        
        result = safe_division(10.0, 2)
        self.assertEqual(result, 5.0)
    
    def test_negative_float_division(self):
        """Test division with negative floats."""
        result = safe_division(-7.5, 2.5)
        self.assertEqual(result, -3.0)
        
        result = safe_division(7.5, -2.5)
        self.assertEqual(result, -3.0)


if __name__ == '__main__':
    unittest.main()
