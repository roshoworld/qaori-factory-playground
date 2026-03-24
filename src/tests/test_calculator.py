# tests/test_calculator.py
import pytest
import sys
import os

# Add the src directory to the Python path to allow importing calculator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import add, subtract, multiply, divide, main

# Test cases for the add function
@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (0, 5, 5),
    (10, 0, 10),
    (-5, 10, 5),
    (2.5, 3.5, 6.0),
    (-1.0, 1.0, 0.0),
    (1000000, 2000000, 3000000),
    (0, 0, 0),
])
def test_add(x, y, expected):
    """Test the add function with various integer and float inputs."""
    assert add(x, y) == expected

# Test cases for the subtract function
@pytest.mark.parametrize("x, y, expected", [
    (5, 2, 3),
    (2, 5, -3),
    (-5, -2, -3),
    (-2, -5, 3),
    (10, 0, 10),
    (0, 7, -7),
    (7.5, 2.5, 5.0),
    (-3.0, 1.0, -4.0),
    (0, 0, 0),
])
def test_subtract(x, y, expected):
    """Test the subtract function with various integer and float inputs."""
    assert subtract(x, y) == expected

# Test cases for the multiply function
@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (2, -3, -6),
    (-2, -3, 6),
    (0, 5, 0),
    (5, 0, 0),
    (2.5, 2, 5.0),
    (0.5, 0.5, 0.25),
    (1, 1, 1),
    (-1, 1, -1),
])
def test_multiply(x, y, expected):
    """Test the multiply function with various integer and float inputs."""
    assert multiply(x, y) == expected

# Test cases for the divide function with valid inputs
@pytest.mark.parametrize("x, y, expected", [
    (6, 2, 3.0),
    (10, 3, pytest.approx(3.3333333333333335)), # Use pytest.approx for float comparisons
    (-6, 2, -3.0),
    (6, -2, -3.0),
    (-6, -2, 3.0),
    (0, 5, 0.0),
    (7.5, 2.5, 3.0),
    (1.0, 0.5, 2.0),
    (10, 1, 10.0),
])
def test_divide_valid_inputs(x, y, expected):
    """Test the divide function with various valid integer and float inputs."""
    assert divide(x, y) == expected

def test_divide_by_zero_raises_error():
    """Test that dividing by zero raises a ValueError with the correct message."""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)

def test_divide_zero_by_zero_raises_error():
    """Test that dividing zero by zero also raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(0, 0)

def test_main_function_execution(capsys):
    """
    Test that the main function executes without unhandled exceptions
    and produces expected output, including the caught division by zero error.
    """
    main()
    captured = capsys.readouterr()

    # Assert that the expected output is present
    assert "Simple Calculator Operations:" in captured.out
    assert "10 + 5 = 15" in captured.out
    assert "10 - 5 = 5" in captured.out
    assert "10 * 5 = 50" in captured.out
    assert "10 / 5 = 2.0" in captured.out
    assert "Error: Cannot divide by zero!" in captured.out

    # Ensure no unexpected errors are printed to stderr
    assert captured.err == ""

# Additional checks as per IRON RULE M and general QA practices:
# These are typically run as pre-commit hooks or CI/CD steps, not as part of pytest.
# However, for completeness, a note on how they would be verified:

# 1. Python syntax validation (IRON RULE M):
#    This would be executed via a shell command in CI/CD or a pre-commit hook:
#    `python -m py_compile src/calculator.py`
#    A successful run means no output and exit code 0. A failure would produce syntax errors.

# 2. Direct execution check:
#    This would involve running the script directly and checking its exit code.
#    `python src/calculator.py`
#    Since the main function handles its own ValueError, it should exit cleanly (exit code 0).
#    If it were to crash due to an unhandled exception, the exit code would be non-zero.