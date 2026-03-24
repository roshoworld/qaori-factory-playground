import pytest
import subprocess
import os
from src import calculator

# Test cases for add function
def test_add_positive_numbers():
    # Arrange
    a, b = 2, 3
    expected = 5
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

def test_add_negative_numbers():
    # Arrange
    a, b = -2, -3
    expected = -5
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

def test_add_zero():
    # Arrange
    a, b = 5, 0
    expected = 5
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

def test_add_float_numbers():
    # Arrange
    a, b = 2.5, 3.5
    expected = 6.0
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

# Test cases for subtract function
def test_subtract_positive_numbers():
    # Arrange
    a, b = 5, 2
    expected = 3
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert result == expected

def test_subtract_negative_numbers():
    # Arrange
    a, b = -5, -2
    expected = -3
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert result == expected

def test_subtract_zero():
    # Arrange
    a, b = 5, 0
    expected = 5
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert result == expected

def test_subtract_float_numbers():
    # Arrange
    a, b = 5.5, 2.5
    expected = 3.0
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert result == expected

# Test cases for multiply function
def test_multiply_positive_numbers():
    # Arrange
    a, b = 2, 3
    expected = 6
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert result == expected

def test_multiply_negative_numbers():
    # Arrange
    a, b = -2, -3
    expected = 6
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert result == expected

def test_multiply_by_zero():
    # Arrange
    a, b = 5, 0
    expected = 0
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert result == expected

def test_multiply_float_numbers():
    # Arrange
    a, b = 2.5, 2.0
    expected = 5.0
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert result == expected

# Test cases for divide function
def test_divide_positive_numbers():
    # Arrange
    a, b = 10, 2
    expected = 5.0
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert result == expected

def test_divide_negative_numbers():
    # Arrange
    a, b = -10, 2
    expected = -5.0
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert result == expected

def test_divide_by_one():
    # Arrange
    a, b = 7, 1
    expected = 7.0
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert result == expected

def test_divide_float_numbers():
    # Arrange
    a, b = 10.0, 4.0
    expected = 2.5
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert result == expected

def test_divide_by_zero_raises_value_error():
    # Arrange
    a, b = 5, 0
    expected_message = "Cannot divide by zero"
    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        calculator.divide(a, b)
    assert expected_message in str(excinfo.value)

# Test for IRON RULE M: Python syntax validation
def test_python_syntax_validation():
    """
    Verifies that the src/calculator.py file has no Python syntax errors.
    This directly addresses IRON RULE M.
    """
    # Arrange
    # Get the directory of the current test file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to src/calculator.py relative to the test file
    calculator_file_path = os.path.join(current_dir, '..', 'src', 'calculator.py')

    # Ensure the file exists before attempting to compile
    if not os.path.exists(calculator_file_path):
        pytest.fail(f"Calculator file not found at: {calculator_file_path}")

    # Act
    # Execute python -m py_compile on the calculator.py file
    # The command will return a non-zero exit code if there's a syntax error.
    process = subprocess.run(
        ['python', '-m', 'py_compile', calculator_file_path],
        capture_output=True,
        text=True,
        check=False # Do not raise an exception for non-zero exit codes yet
    )

    # Assert
    # Check if the process completed successfully (exit code 0)
    assert process.returncode == 0, \
        f"Python syntax error found in {calculator_file_path}:\n{process.stderr}"
    # Optionally, check for any output to stderr, though py_compile is usually silent on success
    assert not process.stderr, \
        f"Unexpected stderr output during py_compile:\n{process.stderr}"
