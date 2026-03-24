import pytest
import subprocess
import sys
import os

# Adjust the path to import the calculator module
# Assuming the test file is in 'tests/' and the source is in 'src/'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import calculator

# --- Test for IRON RULE M: Python Syntax Validation (py_compile) ---
def test_calculator_syntax_compiles():
    """
    Verifies that src/calculator.py compiles without syntax errors using py_compile.
    This directly addresses IRON RULE M.
    """
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/calculator.py'))
    
    # Ensure the file exists before attempting to compile
    assert os.path.exists(script_path), f"File not found: {script_path}"

    try:
        # Run py_compile as a subprocess
        result = subprocess.run(
            [sys.executable, "-m", "py_compile", script_path],
            capture_output=True,
            text=True,
            check=True # Raise CalledProcessError if the command returns a non-zero exit code
        )
        # py_compile typically prints nothing to stdout/stderr on success.
        # If it fails, it will raise CalledProcessError due to check=True.
        # We can also check for specific error messages in stderr if needed.
        assert not result.stderr, f"py_compile reported errors:\n{result.stderr}"
        print(f"\npy_compile output (stdout):\n{result.stdout}")
        print(f"py_compile output (stderr):\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        pytest.fail(f"py_compile failed with exit code {e.returncode}:\n{e.stdout}\n{e.stderr}")
    except FileNotFoundError:
        pytest.fail(f"Python executable not found. Is Python installed and in PATH?")


# --- Test for module import (implicit runtime check) ---
def test_calculator_module_imports_without_error():
    """
    Verifies that the calculator module can be imported without runtime errors.
    This implicitly checks for basic runtime stability and function availability.
    """
    # The import is already done at the top of the file.
    # If it failed, pytest would have caught it before reaching this test.
    assert calculator is not None
    assert hasattr(calculator, 'add')
    assert hasattr(calculator, 'subtract')
    assert hasattr(calculator, 'multiply')
    assert hasattr(calculator, 'divide')


# --- Unit tests for arithmetic functions ---

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (0, 5, 5),
    (10.5, 2.5, 13.0),
    (-10.5, 2.5, -8.0),
    (0, 0, 0),
    (1000000, 2000000, 3000000),
    (-100, 50, -50),
])
def test_add(a, b, expected):
    """Tests the add function with various inputs."""
    # Arrange (inputs a, b, expected are provided by parametrize)
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 3),
    (2, 5, -3),
    (-5, -2, -3),
    (0, 5, -5),
    (10.5, 2.5, 8.0),
    (-10.5, 2.5, -13.0),
    (0, 0, 0),
    (100, -50, 150),
])
def test_subtract(a, b, expected):
    """Tests the subtract function with various inputs."""
    # Arrange
    # Act
    result = calculator.subtract(a, b)
    # Assert
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (-2, -3, 6),
    (0, 5, 0),
    (10.5, 2, 21.0),
    (-10.5, 0, 0.0),
    (0, 0, 0),
    (0.5, 0.5, 0.25),
])
def test_multiply(a, b, expected):
    """Tests the multiply function with various inputs."""
    # Arrange
    # Act
    result = calculator.multiply(a, b)
    # Assert
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2.0),
    (7, 2, 3.5),
    (-6, 3, -2.0),
    (-6, -3, 2.0),
    (0, 5, 0.0),
    (10.0, 2.5, 4.0),
    (1, 3, pytest.approx(0.3333333333333333)), # Use pytest.approx for float comparison
    (100, 10, 10.0),
])
def test_divide(a, b, expected):
    """Tests the divide function with various inputs."""
    # Arrange
    # Act
    result = calculator.divide(a, b)
    # Assert
    assert result == expected

def test_divide_by_zero_raises_error():
    """Tests that dividing by zero raises a ValueError."""
    # Arrange (inputs are hardcoded for this specific error case)
    # Act & Assert
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.divide(10, 0)

def test_divide_zero_by_zero_raises_error():
    """Tests that dividing zero by zero raises a ValueError."""
    # Arrange
    # Act & Assert
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.divide(0, 0)

# --- Test for the __main__ block execution ---
def test_main_block_runs_without_error():
    """
    Tests that the __main__ block of calculator.py runs without raising exceptions
    and produces expected output to stdout.
    """
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/calculator.py'))
    
    # Ensure the file exists
    assert os.path.exists(script_path), f"File not found: {script_path}"

    try:
        # Run the script as a subprocess to simulate direct execution
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            check=True # Raise CalledProcessError if the script returns a non-zero exit code
        )
        stdout = result.stdout
        stderr = result.stderr

        # Assertions for expected output
        assert "Qaori Alter Platform - Simple Calculator Utility" in stdout
        assert "Adding 10.5 and 2.5: 13.0" in stdout
        assert "Subtracting 2.5 from 10.5: 8.0" in stdout
        assert "Multiplying 10.5 by 2.5: 26.25" in stdout
        assert "Dividing 10.5 by 2.5: 4.2" in stdout
        assert "Error during division: Cannot divide by zero." in stdout
        assert "Syntax validation check: This file should pass 'python -m py_compile'." in stdout
        
        # Ensure no unexpected errors are printed to stderr
        assert not stderr, f"Script produced unexpected output to stderr:\n{stderr}"

    except subprocess.CalledProcessError as e:
        pytest.fail(f"calculator.py script failed with exit code {e.returncode}:\n{e.stdout}\n{e.stderr}")
    except FileNotFoundError:
        pytest.fail(f"Python executable not found. Is Python installed and in PATH?")