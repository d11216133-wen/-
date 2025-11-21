"""
Safe Division Module

This module provides a safe_division function that handles division by zero gracefully.
"""


def safe_division(a, b):
    """
    Safely divides two numbers, handling division by zero.
    
    Args:
        a: The numerator (dividend)
        b: The denominator (divisor)
    
    Returns:
        The result of a / b if b is not zero
        None if b is zero (to handle division by zero safely)
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
        >>> safe_division(-10, 2)
        -5.0
    """
    try:
        return a / b
    except ZeroDivisionError:
        # Handle division by zero gracefully
        return None
