# tests/test_calculator.py
import pytest
from src.calculator import add, subtract, multiply, divide

# --- Test cases for add function ---
def test_add_positive_integers():
    """Test addition of two positive integers."""
    # Arrange
    a, b = 2, 3
    # Act
    result = add(a, b)
    # Assert
    assert result == 5

def test_add_negative_integers():
    """Test addition of two negative integers."""
    # Arrange
    a, b = -2, -3
    # Act
    result = add(a, b)
    # Assert
    assert result == -5

def test_add_zero_to_number():
    """Test addition with zero."""
    # Arrange
    a, b = 0, 5
    # Act
    result = add(a, b)
    # Assert
    assert result == 5
    # Arrange
    a, b = 5, 0
    # Act
    result = add(a, b)
    # Assert
    assert result == 5

def test_add_mixed_integers():
    """Test addition of positive and negative integers."""
    # Arrange
    a, b = -2, 5
    # Act
    result = add(a, b)
    # Assert
    assert result == 3

def test_add_float_numbers():
    """Test addition of floating-point numbers."""
    # Arrange
    a, b = 2.5, 3.5
    # Act
    result = add(a, b)
    # Assert
    assert result == 6.0

# --- Test cases for subtract function ---
def test_subtract_positive_integers():
    """Test subtraction of two positive integers."""
    # Arrange
    a, b = 5, 2
    # Act
    result = subtract(a, b)
    # Assert
    assert result == 3

def test_subtract_negative_integers():
    """Test subtraction of two negative integers."""
    # Arrange
    a, b = -5, -2
    # Act
    result = subtract(a, b)
    # Assert
    assert result == -3

def test_subtract_zero_from_number():
    """Test subtraction with zero."""
    # Arrange
    a, b = 5, 0
    # Act
    result = subtract(a, b)
    # Assert
    assert result == 5
    # Arrange
    a, b = 0, 5
    # Act
    result = subtract(a, b)
    # Assert
    assert result == -5

def test_subtract_mixed_integers():
    """Test subtraction of positive and negative integers."""
    # Arrange
    a, b = -5, 2
    # Act
    result = subtract(a, b)
    # Assert
    assert result == -7

def test_subtract_float_numbers():
    """Test subtraction of floating-point numbers."""
    # Arrange
    a, b = 5.5, 2.5
    # Act
    result = subtract(a, b)
    # Assert
    assert result == 3.0

# --- Test cases for multiply function ---
def test_multiply_positive_integers():
    """Test multiplication of two positive integers."""
    # Arrange
    a, b = 2, 3
    # Act
    result = multiply(a, b)
    # Assert
    assert result == 6

def test_multiply_negative_integers():
    """Test multiplication of two negative integers."""
    # Arrange
    a, b = -2, -3
    # Act
    result = multiply(a, b)
    # Assert
    assert result == 6

def test_multiply_by_zero():
    """Test multiplication by zero."""
    # Arrange
    a, b = 0, 5
    # Act
    result = multiply(a, b)
    # Assert
    assert result == 0
    # Arrange
    a, b = 5, 0
    # Act
    result = multiply(a, b)
    # Assert
    assert result == 0

def test_multiply_mixed_integers():
    """Test multiplication of positive and negative integers."""
    # Arrange
    a, b = -2, 5
    # Act
    result = multiply(a, b)
    # Assert
    assert result == -10

def test_multiply_float_numbers():
    """Test multiplication of floating-point numbers."""
    # Arrange
    a, b = 2.5, 2.0
    # Act
    result = multiply(a, b)
    # Assert
    assert result == 5.0

# --- Test cases for divide function ---
def test_divide_positive_integers():
    """Test division of two positive integers."""
    # Arrange
    a, b = 10, 2
    # Act
    result = divide(a, b)
    # Assert
    assert result == 5.0

def test_divide_negative_integers():
    """Test division of two negative integers."""
    # Arrange
    a, b = -10, -2
    # Act
    result = divide(a, b)
    # Assert
    assert result == 5.0

def test_divide_mixed_integers():
    """Test division of positive and negative integers."""
    # Arrange
    a, b = -10, 2
    # Act
    result = divide(a, b)
    # Assert
    assert result == -5.0

def test_divide_float_numbers():
    """Test division of floating-point numbers."""
    # Arrange
    a, b = 10.0, 2.5
    # Act
    result = divide(a, b)
    # Assert
    assert result == 4.0

def test_divide_zero_by_number():
    """Test division of zero by a non-zero number."""
    # Arrange
    a, b = 0, 5
    # Act
    result = divide(a, b)
    # Assert
    assert result == 0.0

def test_divide_by_one():
    """Test division by one."""
    # Arrange
    a, b = 7, 1
    # Act
    result = divide(a, b)
    # Assert
    assert result == 7.0

def test_divide_by_zero_raises_value_error():
    """Test that division by zero raises a ValueError."""
    # Arrange
    a, b = 10, 0
    # Act & Assert
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(a, b)
