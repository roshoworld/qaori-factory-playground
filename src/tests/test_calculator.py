# File: src/calculator.py
# (This file is provided by the user and assumed to be located at src/calculator.py)

# Calculator module
def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return a times b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# File: tests/test_calculator.py
# (This file should be placed in a 'tests' directory: tests/test_calculator.py)

import pytest
from src import calculator

def test_add_positive_numbers():
    """Test addition with two positive numbers."""
    assert calculator.add(2, 3) == 5

def test_add_negative_numbers():
    """Test addition with two negative numbers."""
    assert calculator.add(-1, -5) == -6

def test_add_mixed_numbers():
    """Test addition with mixed positive and negative numbers."""
    assert calculator.add(10, -3) == 7

def test_add_with_zero():
    """Test addition with zero."""
    assert calculator.add(0, 7) == 7

def test_add_float_numbers():
    """Test addition with float numbers."""
    assert calculator.add(0.1, 0.2) == pytest.approx(0.3)

def test_subtract_positive_numbers():
    """Test subtraction with two positive numbers."""
    assert calculator.subtract(5, 2) == 3

def test_subtract_negative_numbers():
    """Test subtraction with two negative numbers."""
    assert calculator.subtract(-1, -5) == 4

def test_subtract_mixed_numbers():
    """Test subtraction with mixed positive and negative numbers."""
    assert calculator.subtract(10, -3) == 13

def test_subtract_with_zero():
    """Test subtraction with zero."""
    assert calculator.subtract(7, 0) == 7
    assert calculator.subtract(0, 7) == -7

def test_subtract_float_numbers():
    """Test subtraction with float numbers."""
    assert calculator.subtract(0.5, 0.1) == pytest.approx(0.4)

def test_multiply_positive_numbers():
    """Test multiplication with two positive numbers."""
    assert calculator.multiply(2, 3) == 6

def test_multiply_negative_numbers():
    """Test multiplication with two negative numbers."""
    assert calculator.multiply(-2, -3) == 6

def test_multiply_mixed_numbers():
    """Test multiplication with mixed positive and negative numbers."""
    assert calculator.multiply(2, -3) == -6

def test_multiply_with_zero():
    """Test multiplication with zero."""
    assert calculator.multiply(0, 5) == 0
    assert calculator.multiply(5, 0) == 0

def test_multiply_with_one():
    """Test multiplication with one."""
    assert calculator.multiply(5, 1) == 5

def test_multiply_float_numbers():
    """Test multiplication with float numbers."""
    assert calculator.multiply(2.5, 2) == 5.0

def test_divide_positive_numbers():
    """Test division with two positive numbers."""
    assert calculator.divide(6, 2) == 3.0

def test_divide_negative_numbers():
    """Test division with two negative numbers."""
    assert calculator.divide(-6, -2) == 3.0

def test_divide_mixed_numbers():
    """Test division with mixed positive and negative numbers."""
    assert calculator.divide(6, -2) == -3.0

def test_divide_fractional_result():
    """Test division resulting in a float."""
    assert calculator.divide(5, 2) == 2.5

def test_divide_zero_dividend():
    """Test division with zero as the dividend."""
    assert calculator.divide(0, 5) == 0.0

def test_divide_by_zero_raises_error():
    """Test that division by zero raises a ValueError."""
    with pytest.raises(ValueError) as excinfo:
        calculator.divide(5, 0)
    assert "Cannot divide by zero" in str(excinfo.value)

# File: run_tests.py
# (This script should be placed in the project root directory)

import os
import sys
import py_compile
import subprocess

# Define paths
SRC_DIR = "src"
TESTS_DIR = "tests"
CALCULATOR_FILE = os.path.join(SRC_DIR, "calculator.py")
TEST_CALCULATOR_FILE = os.path.join(TESTS_DIR, "test_calculator.py")

# Content of src/calculator.py (as provided by the user)
calculator_content = """# Calculator module
def add(a, b):
    \"\"\"Return the sum of a and b.\"\"\"
    return a + b


def subtract(a, b):
    \"\"\"Return a minus b.\"\"\"
    return a - b


def multiply(a, b):
    \"\"\"Return a times b.\"\"\"
    return a * b


def divide(a, b):
    \"\"\"Return a divided by b. Raises ValueError if b is zero.\"\"\"
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b"""

# Content of tests/test_calculator.py (generated above)
test_calculator_content = """import pytest
from src import calculator

def test_add_positive_numbers():
    \"\"\"Test addition with two positive numbers.\"\"\"
    assert calculator.add(2, 3) == 5

def test_add_negative_numbers():
    \"\"\"Test addition with two negative numbers.\"\"\"
    assert calculator.add(-1, -5) == -6

def test_add_mixed_numbers():
    \"\"\"Test addition with mixed positive and negative numbers.\"\"\"
    assert calculator.add(10, -3) == 7

def test_add_with_zero():
    \"\"\"Test addition with zero.\"\"\"
    assert calculator.add(0, 7) == 7

def test_add_float_numbers():
    \"\"\"Test addition with float numbers.\"\"\"
    assert calculator.add(0.1, 0.2) == pytest.approx(0.3)

def test_subtract_positive_numbers():
    \"\"\"Test subtraction with two positive numbers.\"\"\"
    assert calculator.subtract(5, 2) == 3

def test_subtract_negative_numbers():
    \"\"\"Test subtraction with two negative numbers.\"\"\"
    assert calculator.subtract(-1, -5) == 4

def test_subtract_mixed_numbers():
    \"\"\"Test subtraction with mixed positive and negative numbers.\"\"\"
    assert calculator.subtract(10, -3) == 13

def test_subtract_with_zero():
    \"\"\"Test subtraction with zero.\"\"\"
    assert calculator.subtract(7, 0) == 7
    assert calculator.subtract(0, 7) == -7

def test_subtract_float_numbers():
    \"\"\"Test subtraction with float numbers.\"\"\"
    assert calculator.subtract(0.5, 0.1) == pytest.approx(0.4)

def test_multiply_positive_numbers():
    \"\"\"Test multiplication with two positive numbers.\"\"\"
    assert calculator.multiply(2, 3) == 6

def test_multiply_negative_numbers():
    \"\"\"Test multiplication with two negative numbers.\"\"\"
    assert calculator.multiply(-2, -3) == 6

def test_multiply_mixed_numbers():
    \"\"\"Test multiplication with mixed positive and negative numbers.\"\"\"
    assert calculator.multiply(2, -3) == -6

def test_multiply_with_zero():
    \"\"\"Test multiplication with zero.\"\"\"
    assert calculator.multiply(0, 5) == 0
    assert calculator.multiply(5, 0) == 0

def test_multiply_with_one():
    \"\"\"Test multiplication with one.\"\"\"
    assert calculator.multiply(5, 1) == 5

def test_multiply_float_numbers():
    \"\"\"Test multiplication with float numbers.\"\"\"
    assert calculator.multiply(2.5, 2) == 5.0

def test_divide_positive_numbers():
    \"\"\"Test division with two positive numbers.\"\"\"
    assert calculator.divide(6, 2) == 3.0

def test_divide_negative_numbers():
    \"\"\"Test division with two negative numbers.\"\"\"
    assert calculator.divide(-6, -2) == 3.0

def test_divide_mixed_numbers():
    \"\"\"Test division with mixed positive and negative numbers.\"\"\"
    assert calculator.divide(6, -2) == -3.0

def test_divide_fractional_result():
    \"\"\"Test division resulting in a float.\"\"\"
    assert calculator.divide(5, 2) == 2.5

def test_divide_zero_dividend():
    \"\"\"Test division with zero as the dividend.\"\"\"
    assert calculator.divide(0, 5) == 0.0

def test_divide_by_zero_raises_error():
    \"\"\"Test that division by zero raises a ValueError.\"\"\"
    with pytest.raises(ValueError) as excinfo:
        calculator.divide(5, 0)
    assert "Cannot divide by zero" in str(excinfo.value)
"""

def setup_environment():
    """Create necessary directories and files."""
    os.makedirs(SRC_DIR, exist_ok=True)
    os.makedirs(TESTS_DIR, exist_ok=True)

    with open(CALCULATOR_FILE, "w") as f:
        f.write(calculator_content)
    print(f"Created {CALCULATOR_FILE}")

    with open(TEST_CALCULATOR_FILE, "w") as f:
        f.write(test_calculator_content)
    print(f"Created {TEST_CALCULATOR_FILE}")

def run_syntax_validation():
    """
    Run 'python -m py_compile src/calculator.py' to ensure syntax is valid.
    (Adheres to IRON RULE M)
    """
    print("\n--- Running Python Syntax Validation (IRON RULE M) ---")
    try:
        py_compile.compile(CALCULATOR_FILE, doraise=True)
        print(f"✅ Syntax check passed for {CALCULATOR_FILE}")
        return True
    except py_compile.PyCompileError as e:
        print(f"❌ Syntax check failed for {CALCULATOR_FILE}: {e}")
        return False
    except Exception as e:
        print(f"❌ An unexpected error occurred during syntax check: {e}")
        return False

def run_unit_tests():
    """
    Execute pytest for comprehensive unit testing.
    """
    print("\n--- Running Unit Tests with Pytest ---")
    # Add src/ to Python path for imports
    if SRC_DIR not in sys.path:
        sys.path.insert(0, SRC_DIR)

    try:
        # Run pytest with coverage report
        result = subprocess.run(
            [sys.executable, "-m", "pytest", TESTS_DIR, "--cov=src", "--cov-report=term-missing"],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        print("✅ All unit tests passed.")
        return True
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        print(e.stderr)
        print("❌ Some unit tests failed.")
        return False
    except FileNotFoundError:
        print("❌ pytest command not found. Please ensure pytest is installed (`pip install pytest pytest-cov`).")
        return False
    except Exception as e:
        print(f"❌ An unexpected error occurred during pytest execution: {e}")
        return False

if __name__ == "__main__":
    print("Setting up test environment...")
    setup_environment()

    # Step 1: Run syntax validation
    if not run_syntax_validation():
        print("\n--- Test execution aborted due to syntax errors. ---")
        sys.exit(1)

    # Step 2: Run unit tests
    if not run_unit_tests():
        print("\n--- Test execution completed with failures. ---")
        sys.exit(1)

    print("\n--- All checks and tests passed successfully! ---")
    sys.exit(0)