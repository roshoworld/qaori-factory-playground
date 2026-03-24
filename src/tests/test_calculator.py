# test_calculator.py
import pytest
from src import calculator

# Test cases for the add function
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (-5, -2, -7),
    (100, 200, 300),
    (0.1, 0.2, pytest.approx(0.3)),  # Use pytest.approx for float comparisons
    (10.5, 20.5, 31.0),
    (0, 5, 5),
    (5, 0, 5),
    (-10, 5, -5),
    (5, -10, -5),
])
def test_add(a: float, b: float, expected: float):
    """
    Test cases for the add function.
    AAA Pattern: Arrange (parameters), Act (call function), Assert (check result).
    """
    # Arrange is handled by @pytest.mark.parametrize
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

# Test cases for the subtract function
@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 3),
    (0, 0, 0),
    (1, -1, 2),
    (-5, -2, -3),
    (200, 100, 100),
    (0.5, 0.3, pytest.approx(0.2)),
    (10.0, 5.5, 4.5),
    (0, 5, -5),
    (5, 0, 5),
    (-10, 5, -15),
    (5, -10, 15),
])
def test_subtract(a: float, b: float, expected: float):
    """
    Test cases for the subtract function.
    """
    result = calculator.subtract(a, b)
    assert result == expected

# Test cases for the multiply function
@pytest.mark.parametrize("a, b, expected", [
    (4, 6, 24),
    (5, 0, 0),
    (0, 5, 0),
    (-3, 2, -6),
    (-4, -5, 20),
    (2.5, 2, 5.0),
    (1.5, 0.5, pytest.approx(0.75)),
    (100, 10, 1000),
    (-10, 10, -100),
    (10, -10, -100),
])
def test_multiply(a: float, b: float, expected: float):
    """
    Test cases for the multiply function.
    """
    result = calculator.multiply(a, b)
    assert result == expected

# Test cases for the divide function
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (5.0, 2.0, 2.5),
    (-10, 2, -5.0),
    (-10, -2, 5.0),
    (0, 5, 0.0),
    (100, 10, 10.0),
    (1, 3, pytest.approx(0.3333333333333333)),
])
def test_divide_success(a: float, b: float, expected: float):
    """
    Test cases for successful division.
    """
    result = calculator.divide(a, b)
    assert result == expected

def test_divide_by_zero():
    """
    Test case for division by zero, which should raise a ValueError.
    """
    # Act & Assert
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.divide(7, 0)

    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.divide(0, 0)

    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.divide(-5, 0)