# test_calculator.py
import pytest
from src import calculator

# As a senior QA engineer, I acknowledge the broader test scenarios outlined in the project context.
# These unit tests specifically address the functional correctness of the calculator module.
#
# Broader QA Context & IRON RULE M Validation:
# 1.  Local Syntax Validation (IRON RULE M): Before committing, 'python -m py_compile src/calculator.py'
#     MUST be run locally to ensure no syntax errors are introduced. This is typically enforced
#     via a pre-commit hook.
# 2.  Runtime Execution: The 'if __name__ == "__main__":' block in src/calculator.py serves as a basic
#     runtime smoke test. For production services, dedicated smoke tests (Layer 6 of Quality Gates)
#     would be implemented.
# 3.  CI/CD Monitoring: Post-push, Cloud Build logs (Layers 1-7) must be monitored to confirm
#     successful deployment, including Python syntax validation (Layer 2) and post-deployment
#     smoke tests (Layer 6).
# 4.  Service Integration: If this module is part of a larger service, relevant service endpoints
#     would be smoke-tested after deployment to ensure continued functionality.
#
# These unit tests focus on the isolated logic of the calculator functions.

def test_add_positive_numbers():
    """
    Test addition with two positive numbers.
    """
    # Arrange
    a, b = 5.0, 3.0
    expected = 8.0
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

def test_add_negative_numbers():
    """
    Test addition with two negative numbers.
    """
    # Arrange
    a, b = -5.0, -3.0
    expected = -8.0
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

def test_add_mixed_numbers():
    """
    Test addition with a positive and a negative number.
    """
    # Arrange
    a, b = 5.0, -3.0
    expected = 2.0
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

def test_add_with_zero():
    """
    Test addition involving zero.
    """
    # Arrange
    a, b = 7.0, 0.0
    expected = 7.0
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

def test_add_floats():
    """
    Test addition with floating-point numbers.
    """
    # Arrange
    a, b = 0.1, 0.2
    expected = 0.3
    # Act
    result = calculator.add(a, b)
    # Assert
    assert pytest.approx(result) == expected

def test_subtract_positive_numbers():
    """
    Test subtraction with two positive numbers.
    """
    # Arrange
    a, b = 10.0, 4.0
    expected = 6.0
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert result == expected

def test_subtract_negative_numbers():
    """
    Test subtraction with two negative numbers.
    """
    # Arrange
    a, b = -10.0, -4.0
    expected = -6.0
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert result == expected

def test_subtract_mixed_numbers():
    """
    Test subtraction with a positive and a negative number.
    """
    # Arrange
    a, b = 10.0, -4.0
    expected = 14.0
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert result == expected

def test_subtract_with_zero():
    """
    Test subtraction involving zero.
    """
    # Arrange
    a, b = 8.0, 0.0
    expected = 8.0
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert result == expected

def test_subtract_floats():
    """
    Test subtraction with floating-point numbers.
    """
    # Arrange
    a, b = 0.5, 0.1
    expected = 0.4
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert pytest.approx(result) == expected

def test_multiply_positive_numbers():
    """
    Test multiplication with two positive numbers.
    """
    # Arrange
    a, b = 5.0, 3.0
    expected = 15.0
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert result == expected

def test_multiply_negative_numbers():
    """
    Test multiplication with two negative numbers.
    """
    # Arrange
    a, b = -5.0, -3.0
    expected = 15.0
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert result == expected

def test_multiply_mixed_numbers():
    """
    Test multiplication with a positive and a negative number.
    """
    # Arrange
    a, b = 5.0, -3.0
    expected = -15.0
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert result == expected

def test_multiply_by_zero():
    """
    Test multiplication by zero.
    """
    # Arrange
    a, b = 7.0, 0.0
    expected = 0.0
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert result == expected

def test_multiply_floats():
    """
    Test multiplication with floating-point numbers.
    """
    # Arrange
    a, b = 2.5, 2.0
    expected = 5.0
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert pytest.approx(result) == expected

def test_divide_positive_numbers():
    """
    Test division with two positive numbers.
    """
    # Arrange
    a, b = 10.0, 2.0
    expected = 5.0
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert result == expected

def test_divide_negative_numbers():
    """
    Test division with two negative numbers.
    """
    # Arrange
    a, b = -10.0, -2.0
    expected = 5.0
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert result == expected

def test_divide_mixed_numbers():
    """
    Test division with a positive and a negative number.
    """
    # Arrange
    a, b = 10.0, -2.0
    expected = -5.0
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert result == expected

def test_divide_zero_by_number():
    """
    Test division of zero by a non-zero number.
    """
    # Arrange
    a, b = 0.0, 5.0
    expected = 0.0
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert result == expected

def test_divide_floats():
    """
    Test division with floating-point numbers.
    """
    # Arrange
    a, b = 7.0, 2.0
    expected = 3.5
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert pytest.approx(result) == expected

def test_divide_by_zero_raises_error():
    """
    Test that division by zero raises a ValueError.
    """
    # Arrange
    a, b = 10.0, 0.0
    # Act & Assert
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.divide(a, b)

def test_divide_zero_by_zero_raises_error():
    """
    Test that division of zero by zero also raises a ValueError.
    """
    # Arrange
    a, b = 0.0, 0.0
    # Act & Assert
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.divide(a, b)