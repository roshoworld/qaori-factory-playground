# src/calculator.py

"""
A simple calculator module to demonstrate valid Python syntax
for IRON RULE M validation.
"""

def add(a: float, b: float) -> float:
    """
    Adds two numbers and returns their sum.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first and returns the difference.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers and returns their product.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divides the first number by the second and returns the quotient.
    Raises ValueError if division by zero is attempted.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("--- Simple Calculator Demo ---")

    # Example usage
    x = 10.0
    y = 2.0

    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")
    print(f"{x} / {y} = {divide(x, y)}")

    # Test division by zero
    try:
        print(f"{x} / 0 = {divide(x, 0)}")
    except ValueError as e:
        print(f"Error: {e}")

    print("--- Demo Complete ---")