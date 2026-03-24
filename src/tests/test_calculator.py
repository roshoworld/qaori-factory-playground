# test_calculator.py
import pytest
from src.calculator import add, subtract, multiply, divide, power, modulo

# Test cases for add function
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (1, -2, -1),
    (-1, 2, 1),
    (0, 0, 0),
    (100, 200, 300),
    (0.5, 0.3, 0.8),
    (0, 5, 5),
    (5, 0, 5),
])
def test_add(a, b, expected):
    """
    Test cases for the add function.
    Arrange: Define input numbers (a, b) and expected sum.
    Act: Call the add function with a and b.
    Assert: Verify the result matches the expected sum.
    """
    result = add(a, b)
    assert result == expected

# Test cases for subtract function
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (3, 5, -2),
    (-5, -3, -2),
    (-3, -5, 2),
    (5, -3, 8),
    (-5, 3, -8),
    (0, 0, 0),
    (100, 50, 50),
    (0.7, 0.2, 0.5),
    (0, 5, -5),
    (5, 0, 5),
])
def test_subtract(a, b, expected):
    """
    Test cases for the subtract function.
    Arrange: Define input numbers (a, b) and expected difference.
    Act: Call the subtract function with a and b.
    Assert: Verify the result matches the expected difference.
    """
    result = subtract(a, b)
    assert result == expected

# Test cases for multiply function
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (2, -3, -6),
    (-2, -3, 6),
    (0, 5, 0),
    (5, 0, 0),
    (0, 0, 0),
    (10, 10, 100),
    (0.5, 4, 2.0),
    (0.1, 0.2, 0.02),
])
def test_multiply(a, b, expected):
    """
    Test cases for the multiply function.
    Arrange: Define input numbers (a, b) and expected product.
    Act: Call the multiply function with a and b.
    Assert: Verify the result matches the expected product.
    """
    result = multiply(a, b)
    assert result == expected

# Test cases for divide function
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2.0),
    (7, 2, 3.5),
    (-6, 3, -2.0),
    (6, -3, -2.0),
    (-6, -3, 2.0),
    (0, 5, 0.0),
    (10, 4, 2.5),
    (1, 3, 1/3),
])
def test_divide_success(a, b, expected):
    """
    Test cases for the divide function (success paths).
    Arrange: Define input numbers (a, b) and expected quotient.
    Act: Call the divide function with a and b.
    Assert: Verify the result matches the expected quotient.
    """
    result = divide(a, b)
    assert result == expected

def test_divide_by_zero_error():
    """
    Test case for the divide function (error state: division by zero).
    Arrange: Define input numbers where b is zero.
    Act: Call the divide function.
    Assert: Verify that a ValueError is raised with the correct message.
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# Test cases for power function
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (10, 1, 10),
    (2, -1, 0.5),
    (-2, 3, -8),
    (-2, 2, 4),
    (0, 5, 0),
    (0, 0, 1), # Python's 0**0 is 1
    (4, 0.5, 2.0), # Square root
    (9, 0.5, 3.0),
])
def test_power(a, b, expected):
    """
    Test cases for the power function.
    Arrange: Define input numbers (a, b) and expected result.
    Act: Call the power function with a and b.
    Assert: Verify the result matches the expected value.
    """
    result = power(a, b)
    assert result == expected

# Test cases for modulo function
@pytest.mark.parametrize("a, b, expected", [
    (10, 3, 1),
    (10, 2, 0),
    (7, 4, 3),
    (-10, 3, 2), # Python's modulo behavior for negative numbers
    (10, -3, -2),
    (-10, -3, -1),
    (0, 5, 0),
    (5.5, 2.0, 1.5),
])
def test_modulo_success(a, b, expected):
    """
    Test cases for the modulo function (success paths).
    Arrange: Define input numbers (a, b) and expected remainder.
    Act: Call the modulo function with a and b.
    Assert: Verify the result matches the expected remainder.
    """
    result = modulo(a, b)
    assert result == expected

def test_modulo_by_zero_error():
    """
    Test case for the modulo function (error state: modulo by zero).
    Arrange: Define input numbers where b is zero.
    Act: Call the modulo function.
    Assert: Verify that a ValueError is raised with the correct message.
    """
    with pytest.raises(ValueError, match="Cannot perform modulo with zero divisor"):
        modulo(10, 0)

# To run these tests:
# 1. Make sure you have pytest installed: pip install pytest
# 2. Save the calculator.py file in a 'src' directory.
# 3. Save this test_calculator.py file in the root directory or a 'tests' directory.
# 4. Run pytest from your terminal in the project root: pytest