"""
Module containing the safe_division function.
This function performs division with proper error handling.
"""


def safe_division(a, b):
    """
    Performs safe division of two numbers.
    
    Args:
        a: The dividend (numerator)
        b: The divisor (denominator)
    
    Returns:
        The result of a divided by b, or None if division by zero
    
    Raises:
        TypeError: If inputs are not numeric types
    """
    # Check if inputs are numeric
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numeric (int or float)")
    
    # Handle division by zero
    if b == 0:
        return None
    
    # Perform the division
    return a / b
