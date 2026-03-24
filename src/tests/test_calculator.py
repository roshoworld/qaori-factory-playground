# test_calculator.py
import pytest
from src.calculator import add, subtract, multiply, divide

# --- Test cases for add function ---
def test_add_positive_numbers_returns_five():
    """Verify that add(2, 3) returns 5."""
    # Arrange
    a = 2
    b = 3
    expected = 5
    # Act
    result = add(a, b)
    # Assert
    assert result == expected

def test_add_zero_and_positive_returns_five():
    """Verify that add(0, 5) returns 5."""
    # Arrange
    a = 0
    b = 5
    expected = 5
    # Act
    result = add(a, b)
    # Assert
    assert result == expected

def test_add_negative_and_positive_returns_five():
    """Verify that add(-2, 7) returns 5."""
    # Arrange
    a = -2
    b = 7
    expected = 5
    # Act
    result = add(a, b)
    # Assert
    assert result == expected

def test_add_two_negative_numbers():
    """Test adding two negative numbers."""
    # Arrange
    a = -5
    b = -3
    expected = -8
    # Act
    result = add(a, b)
    # Assert
    assert result == expected

def test_add_float_numbers():
    """Test adding float numbers."""
    # Arrange
    a = 0.1
    b = 0.2
    expected = 0.3
    # Act
    result = add(a, b)
    # Assert
    assert result == pytest.approx(expected)

# --- Test cases for subtract function ---
def test_subtract_positive_numbers():
    """Test subtracting positive numbers."""
    # Arrange
    a = 5
    b = 3
    expected = 2
    # Act
    result = subtract(a, b)
    # Assert
    assert result == expected

def test_subtract_negative_numbers():
    """Test subtracting negative numbers."""
    # Arrange
    a = -5
    b = -3
    expected = -2
    # Act
    result = subtract(a, b)
    # Assert
    assert result == expected

def test_subtract_from_zero():
    """Test subtracting from zero."""
    # Arrange
    a = 0
    b = 5
    expected = -5
    # Act
    result = subtract(a, b)
    # Assert
    assert result == expected

def test_subtract_zero():
    """Test subtracting zero."""
    # Arrange
    a = 5
    b = 0
    expected = 5
    # Act
    result = subtract(a, b)
    # Assert
    assert result == expected

# --- Test cases for multiply function ---
def test_multiply_positive_numbers():
    """Test multiplying positive numbers."""
    # Arrange
    a = 2
    b = 3
    expected = 6
    # Act
    result = multiply(a, b)
    # Assert
    assert result == expected

def test_multiply_by_zero():
    """Test multiplying by zero."""
    # Arrange
    a = 5
    b = 0
    expected = 0
    # Act
    result = multiply(a, b)
    # Assert
    assert result == expected

def test_multiply_negative_and_positive():
    """Test multiplying a negative and a positive number."""
    # Arrange
    a = -2
    b = 3
    expected = -6
    # Act
    result = multiply(a, b)
    # Assert
    assert result == expected

def test_multiply_two_negative_numbers():
    """Test multiplying two negative numbers."""
    # Arrange
    a = -2
    b = -3
    expected = 6
    # Act
    result = multiply(a, b)
    # Assert
    assert result == expected

# --- Test cases for divide function ---
def test_divide_positive_numbers():
    """Test dividing positive numbers."""
    # Arrange
    a = 6
    b = 3
    expected = 2.0
    # Act
    result = divide(a, b)
    # Assert
    assert result == expected

def test_divide_by_one():
    """Test dividing by one."""
    # Arrange
    a = 5
    b = 1
    expected = 5.0
    # Act
    result = divide(a, b)
    # Assert
    assert result == expected

def test_divide_zero_numerator():
    """Test dividing zero by a non-zero number."""
    # Arrange
    a = 0
    b = 5
    expected = 0.0
    # Act
    result = divide(a, b)
    # Assert
    assert result == expected

def test_divide_negative_numbers():
    """Test dividing a negative number by a positive number."""
    # Arrange
    a = -6
    b = 3
    expected = -2.0
    # Act
    result = divide(a, b)
    # Assert
    assert result == expected

def test_divide_by_zero_raises_value_error():
    """Test that dividing by zero raises a ValueError."""
    # Arrange
    a = 5
    b = 0
    # Act & Assert
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(a, b)

def test_divide_float_numbers():
    """Test dividing float numbers."""
    # Arrange
    a = 7.0
    b = 2.0
    expected = 3.5
    # Act
    result = divide(a, b)
    # Assert
    assert result == expected