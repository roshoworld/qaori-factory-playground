# src/calculator.py
#
# This file provides basic arithmetic functions.
# Its primary purpose in the context of the Qaori Alter Platform is to serve as a
# standard Python file whose syntax is validated by the 'py_compile' tool
# as part of IRON RULE M (Python Syntax Validation).

def add(a: float, b: float) -> float:
    """
    Adds two numbers and returns the sum.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first and returns the difference.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers and returns the product.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divides the first number by the second and returns the quotient.
    Raises a ValueError if division by zero is attempted.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Qaori Alter Platform - Simple Calculator Utility")
    print("-------------------------------------------------")

    num1 = 10.5
    num2 = 2.5

    print(f"Adding {num1} and {num2}: {add(num1, num2)}")
    print(f"Subtracting {num2} from {num1}: {subtract(num1, num2)}")
    print(f"Multiplying {num1} by {num2}: {multiply(num1, num2)}")

    try:
        print(f"Dividing {num1} by {num2}: {divide(num1, num2)}")
        print(f"Dividing {num1} by 0: {divide(num1, 0)}") # This will raise an error
    except ValueError as e:
        print(f"Error during division: {e}")

    print("\nSyntax validation check: This file should pass 'python -m py_compile'.")