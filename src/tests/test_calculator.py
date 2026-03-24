import pytest
from src.calculator import add, subtract, multiply, divide

# Test cases for the add function
def test_add_positive_numbers():
    # Arrange
    a = 5
    b = 3
    expected_sum = 8

    # Act
    result = add(a, b)

    # Assert
    assert result == expected_sum

def test_add_negative_numbers():
    # Arrange
    a = -5
    b = -3
    expected_sum = -8

    # Act
    result = add(a, b)

    # Assert
    assert result == expected_sum

def test_add_positive_and_negative_numbers():
    # Arrange
    a = 10
    b = -7
    expected_sum = 3

    # Act
    result = add(a, b)

    # Assert
    assert result == expected_sum

def test_add_zero():
    # Arrange
    a = 0
    b = 5
    expected_sum = 5

    # Act
    result = add(a, b)

    # Assert
    assert result == expected_sum

# Test cases for the subtract function
def test_subtract_positive_numbers():
    # Arrange
    a = 10
    b = 4
    expected_difference = 6

    # Act
    result = subtract(a, b)

    # Assert
    assert result == expected_difference

def test_subtract_negative_numbers():
    # Arrange
    a = -5
    b = -2
    expected_difference = -3

    # Act
    result = subtract(a, b)

    # Assert
    assert result == expected_difference

def test_subtract_zero():
    # Arrange
    a = 7
    b = 0
    expected_difference = 7

    # Act
    result = subtract(a, b)

    # Assert
    assert result == expected_difference

# Test cases for the multiply function
def test_multiply_positive_numbers():
    # Arrange
    a = 6
    b = 7
    expected_product = 42

    # Act
    result = multiply(a, b)

    # Assert
    assert result == expected_product

def test_multiply_negative_numbers():
    # Arrange
    a = -4
    b = -5
    expected_product = 20

    # Act
    result = multiply(a, b)

    # Assert
    assert result == expected_product

def test_multiply_by_zero():
    # Arrange
    a = 9
    b = 0
    expected_product = 0

    # Act
    result = multiply(a, b)

    # Assert
    assert result == expected_product

# Test cases for the divide function
def test_divide_positive_numbers():
    # Arrange
    a = 10
    b = 2
    expected_quotient = 5.0

    # Act
    result = divide(a, b)

    # Assert
    assert result == expected_quotient

def test_divide_by_zero_raises_error():
    # Arrange
    a = 10
    b = 0

    # Act & Assert
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(a, b)

def test_divide_zero_by_positive_number():
    # Arrange
    a = 0
    b = 5
    expected_quotient = 0.0

    # Act
    result = divide(a, b)

    # Assert
    assert result == expected_quotient

def test_divide_negative_by_positive_number():
    # Arrange
    a = -10
    b = 2
    expected_quotient = -5.0

    # Act
    result = divide(a, b)

    # Assert
    assert result == expected_quotient

def test_divide_float_numbers():
    # Arrange
    a = 7.5
    b = 2.5
    expected_quotient = 3.0

    # Act
    result = divide(a, b)

    # Assert
    assert result == expected_quotient