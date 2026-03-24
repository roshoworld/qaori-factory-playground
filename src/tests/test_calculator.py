# tests/test_calculator.py
import pytest
import sys
import os

# Add the src directory to the Python path to allow importing calculator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import calculator

# --- Test Scenario 3: Verify functionality works as expected without runtime errors ---

def test_add_positive_numbers():
    """
    AAA Pattern: Arrange, Act, Assert
    Arrange: Define inputs (a=2, b=3)
    Act: Call the add function
    Assert: Verify the output is 5
    """
    assert calculator.add(2, 3) == 5

def test_add_negative_numbers():
    assert calculator.add(-1, -5) == -6

def test_add_zero():
    assert calculator.add(0, 7) == 7
    assert calculator.add(-10, 0) == -10

def test_add_float_numbers():
    assert calculator.add(2.5, 3.5) == 6.0
    assert calculator.add(1.1, 2.2) == pytest.approx(3.3)

def test_subtract_positive_numbers():
    assert calculator.subtract(5, 2) == 3

def test_subtract_negative_numbers():
    assert calculator.subtract(-5, -2) == -3
    assert calculator.subtract(2, 5) == -3

def test_subtract_zero():
    assert calculator.subtract(10, 0) == 10
    assert calculator.subtract(0, 5) == -5

def test_subtract_float_numbers():
    assert calculator.subtract(5.5, 2.5) == 3.0
    assert calculator.subtract(3.3, 1.1) == pytest.approx(2.2)

def test_multiply_positive_numbers():
    assert calculator.multiply(4, 6) == 24

def test_multiply_negative_numbers():
    assert calculator.multiply(-4, 6) == -24
    assert calculator.multiply(-4, -6) == 24

def test_multiply_zero():
    assert calculator.multiply(0, 5) == 0
    assert calculator.multiply(10, 0) == 0

def test_multiply_float_numbers():
    assert calculator.multiply(2.5, 2.0) == 5.0
    assert calculator.multiply(1.5, 2.5) == pytest.approx(3.75)

def test_divide_positive_numbers():
    assert calculator.divide(10, 2) == 5.0

def test_divide_negative_numbers():
    assert calculator.divide(-10, 2) == -5.0
    assert calculator.divide(10, -2) == -5.0
    assert calculator.divide(-10, -2) == 5.0

def test_divide_by_one():
    assert calculator.divide(7, 1) == 7.0

def test_divide_zero_by_number():
    assert calculator.divide(0, 5) == 0.0

def test_divide_float_numbers():
    assert calculator.divide(7.5, 2.5) == 3.0
    assert calculator.divide(10.0, 3.0) == pytest.approx(3.333333)

def test_divide_by_zero_raises_error():
    """
    Test for the error state: division by zero.
    """
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        calculator.divide(10, 0)

# --- Test Scenario 1: Verify Python file compiles locally using `python -m py_compile` ---
# This is a system-level check, typically run as a pre-commit hook or CI/CD step.
# We simulate this by attempting to import the module, which would fail if there's a syntax error.
# However, for explicit py_compile, a separate script is more appropriate.
# The following script can be placed in `scripts/validate_python_syntax.py`

# scripts/validate_python_syntax.py
import subprocess
import sys
import os

def validate_calculator_syntax():
    """
    Validates the syntax of src/calculator.py using python -m py_compile.
    This directly addresses Test Scenario 1.
    """
    file_to_compile = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/calculator.py'))
    print(f"Running python -m py_compile on {file_to_compile}")
    
    # Use subprocess to run the py_compile command
    result = subprocess.run(
        [sys.executable, "-m", "py_compile", file_to_compile],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"✅ Python syntax validation passed for {file_to_compile}")
        return True
    else:
        print(f"❌ Python syntax validation FAILED for {file_to_compile}")
        print("--- STDOUT ---")
        print(result.stdout)
        print("--- STDERR ---")
        print(result.stderr)
        return False

if __name__ == "__main__":
    if not validate_calculator_syntax():
        sys.exit(1) # Exit with a non-zero code to indicate failure in CI/CD or pre-commit

# --- Test Scenario 2: Monitor Cloud Build logs for Layer 2: Python Syntax Validation ---
# This scenario is about monitoring the CI/CD pipeline.
# The `scripts/validate_python_syntax.py` script, when integrated into the Cloud Build configuration
# (e.g., in `cloudbuild.yaml` as a step before Docker build, as per IRON RULE M),
# will ensure that Layer 2 passes. The monitoring aspect is done by observing the Cloud Build logs
# for the output of this script and the overall step status.
# No direct unit test can "monitor" Cloud Build logs, but ensuring the local check passes
# is the prerequisite for the CI/CD step to pass.