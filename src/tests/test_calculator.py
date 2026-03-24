import pytest
from src import calculator

# Tests for add function
def test_add_positive_numbers():
    # Arrange
    a, b = 2, 3
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == 5

def test_add_negative_numbers():
    assert calculator.add(-1, -5) == -6

def test_add_positive_and_negative():
    assert calculator.add(10, -3) == 7

def test_add_zero():
    assert calculator.add(0, 7) == 7
    assert calculator.add(7, 0) == 7
    assert calculator.add(0, 0) == 0

# Tests for subtract function
def test_subtract_positive_numbers():
    assert calculator.subtract(5, 2) == 3

def test_subtract_negative_numbers():
    assert calculator.subtract(-1, -5) == 4

def test_subtract_positive_and_negative():
    assert calculator.subtract(10, -3) == 13

def test_subtract_zero():
    assert calculator.subtract(7, 0) == 7
    assert calculator.subtract(0, 7) == -7
    assert calculator.subtract(0, 0) == 0

# Tests for multiply function
def test_multiply_positive_numbers():
    assert calculator.multiply(2, 3) == 6

def test_multiply_negative_numbers():
    assert calculator.multiply(-2, -3) == 6

def test_multiply_positive_and_negative():
    assert calculator.multiply(2, -3) == -6

def test_multiply_by_zero():
    assert calculator.multiply(5, 0) == 0
    assert calculator.multiply(0, 5) == 0
    assert calculator.multiply(0, 0) == 0

# Tests for divide function
def test_divide_positive_numbers():
    assert calculator.divide(6, 3) == 2.0

def test_divide_negative_numbers():
    assert calculator.divide(-6, -3) == 2.0

def test_divide_positive_and_negative():
    assert calculator.divide(6, -3) == -2.0

def test_divide_by_one():
    assert calculator.divide(5, 1) == 5.0

def test_divide_zero_by_number():
    assert calculator.divide(0, 5) == 0.0

def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(5, 0)

# Tests for power function (covering all specified scenarios and more)
def test_power_positive_base_positive_exponent():
    # Verify power(2, 3) returns 8.
    assert calculator.power(2, 3) == 8

def test_power_positive_base_zero_exponent():
    # Verify power(5, 0) returns 1.
    assert calculator.power(5, 0) == 1

def test_power_positive_base_one_exponent():
    # Verify power(10, 1) returns 10.
    assert calculator.power(10, 1) == 10

def test_power_positive_base_negative_exponent():
    # Verify power(2, -2) returns 0.25 (1/4).
    assert calculator.power(2, -2) == 0.25

def test_power_zero_base_positive_exponent():
    # Verify power(0, 5) returns 0.
    assert calculator.power(0, 5) == 0

def test_power_zero_base_zero_exponent():
    # Verify power(0, 0) returns 1 (standard mathematical convention).
    assert calculator.power(0, 0) == 1

def test_power_float_base_positive_exponent():
    # Verify power(1.5, 2) returns 2.25.
    assert calculator.power(1.5, 2) == 2.25

def test_power_negative_base_even_exponent():
    assert calculator.power(-2, 2) == 4

def test_power_negative_base_odd_exponent():
    assert calculator.power(-2, 3) == -8

def test_power_negative_base_zero_exponent():
    assert calculator.power(-5, 0) == 1

def test_power_one_base():
    assert calculator.power(1, 100) == 1
    assert calculator.power(1, -100) == 1

def test_power_large_numbers():
    assert calculator.power(2, 10) == 1024