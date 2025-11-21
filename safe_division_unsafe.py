"""
Safe Division Module - WITHOUT Error Handling (for demonstration)

This version DOES NOT handle division by zero - used to demonstrate test failures.
This file is for demonstration purposes only to show what happens when
the safety mechanism is removed.
"""


def safe_division(a, b):
    """
    Division without safety mechanism (UNSAFE VERSION)
    
    This version will raise ZeroDivisionError when b is zero.
    """
    # No try-except block - this will cause ZeroDivisionError
    return a / b
