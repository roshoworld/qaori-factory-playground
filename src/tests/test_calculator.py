import pytest
from src import calculator

# Test cases for add function
def test_add_positive_numbers():
    # Arrange
    a = 5
    b = 3
    expected = 8
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

def test_add_negative_numbers():
    # Arrange
    a = -5
    b = -3
    expected = -8
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

def test_add_positive_and_negative():
    # Arrange
    a = 10
    b = -7
    expected = 3
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

def test_add_zero():
    # Arrange
    a = 7
    b = 0
    expected = 7
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

# Test cases for subtract function
def test_subtract_positive_numbers():
    # Arrange
    a = 10
    b = 4
    expected = 6
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert result == expected

def test_subtract_negative_numbers():
    # Arrange
    a = -5
    b = -2
    expected = -3
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert result == expected

def test_subtract_positive_from_negative():
    # Arrange
    a = -8
    b = 3
    expected = -11
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert result == expected

def test_subtract_zero():
    # Arrange
    a = 5
    b = 0
    expected = 5
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert result == expected

# Test cases for multiply function
def test_multiply_positive_numbers():
    # Arrange
    a = 6
    b = 7
    expected = 42
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert result == expected

def test_multiply_negative_numbers():
    # Arrange
    a = -4
    b = -5
    expected = 20
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert result == expected

def test_multiply_by_zero():
    # Arrange
    a = 9
    b = 0
    expected = 0
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert result == expected

def test_multiply_positive_and_negative():
    # Arrange
    a = 3
    b = -8
    expected = -24
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert result == expected

# Test cases for divide function
def test_divide_positive_numbers():
    # Arrange
    a = 10
    b = 2
    expected = 5.0
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert result == expected

def test_divide_negative_numbers():
    # Arrange
    a = -10
    b = -2
    expected = 5.0
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert result == expected

def test_divide_by_one():
    # Arrange
    a = 7
    b = 1
    expected = 7.0
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert result == expected

def test_divide_zero_by_number():
    # Arrange
    a = 0
    b = 5
    expected = 0.0
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert result == expected

def test_divide_by_zero_raises_error():
    # Arrange
    a = 10
    b = 0
    # Act & Assert
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(a, b)

# Test cases for power function (as per user's specific requirements)
def test_power_positive_integer_exponent():
    # Verify power(2, 3) returns 8.
    # Arrange
    a = 2
    b = 3
    expected = 8
    # Act
    result = calculator.power(a, b)
    # Assert
    assert result == expected

def test_power_zero_exponent():
    # Verify power(5, 0) returns 1.
    # Arrange
    a = 5
    b = 0
    expected = 1
    # Act
    result = calculator.power(a, b)
    # Assert
    assert result == expected

def test_power_base_zero_positive_exponent():
    # Verify power(0, 5) returns 0.
    # Arrange
    a = 0
    b = 5
    expected = 0
    # Act
    result = calculator.power(a, b)
    # Assert
    assert result == expected

def test_power_negative_exponent():
    # Verify power(2, -1) returns 0.5.
    # Arrange
    a = 2
    b = -1
    expected = 0.5
    # Act
    result = calculator.power(a, b)
    # Assert
    assert result == expected

def test_power_fractional_exponent():
    # Verify power(4, 0.5) returns 2.0.
    # Arrange
    a = 4
    b = 0.5
    expected = 2.0
    # Act
    result = calculator.power(a, b)
    # Assert
    assert result == expected

def test_power_zero_to_zero():
    # Verify power(0, 0) returns 1 (standard mathematical convention).
    # Arrange
    a = 0
    b = 0
    expected = 1
    # Act
    result = calculator.power(a, b)
    # Assert
    assert result == expected

def test_power_large_numbers():
    # Verify power(10, 2) returns 100.
    # Arrange
    a = 10
    b = 2
    expected = 100
    # Act
    result = calculator.power(a, b)
    # Assert
    assert result == expected

def test_power_negative_base_even_exponent():
    # Arrange
    a = -2
    b = 2
    expected = 4
    # Act
    result = calculator.power(a, b)
    # Assert
    assert result == expected

def test_power_negative_base_odd_exponent():
    # Arrange
    a = -2
    b = 3
    expected = -8
    # Act
    result = calculator.power(a, b)
    # Assert
    assert result == expected

def test_power_float_base_integer_exponent():
    # Arrange
    a = 2.5
    b = 2
    expected = 6.25
    # Act
    result = calculator.power(a, b)
    # Assert
    assert result == expected