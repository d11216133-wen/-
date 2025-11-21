# Safe Division Function with Unit Tests

This repository contains a Python implementation of a `safe_division` function with comprehensive unit tests.

## Overview

The `safe_division` function performs division with proper error handling:
- Handles division by zero gracefully (returns `None`)
- Validates input types (raises `TypeError` for non-numeric inputs)
- Supports both integers and floats

## Files

- `safe_division.py` - Main module containing the safe_division function
- `test_safe_division.py` - Comprehensive unit tests (13 test cases)

## Usage

```python
from safe_division import safe_division

# Normal division
result = safe_division(10, 2)  # Returns 5.0

# Division by zero
result = safe_division(10, 0)  # Returns None

# Type validation
result = safe_division("10", 2)  # Raises TypeError
```

## Running Tests

Run the unit tests using Python's built-in unittest module:

```bash
python -m unittest test_safe_division.py -v
```

## Test Coverage

The test suite includes 13 comprehensive tests covering:
- ✓ Normal division with positive/negative integers
- ✓ Division with floating point numbers
- ✓ Division by zero scenarios
- ✓ Zero dividend cases
- ✓ Fractional results
- ✓ Very small and very large numbers
- ✓ Type error handling (strings, None, lists)
- ✓ Mixed int/float types

All tests pass successfully!

## Task Completion

This implementation fulfills Task 2: Using Copilot to generate unit tests for `safe_division` and uploading the test code to GitHub.
