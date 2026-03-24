# src/calculator.py

def add(a, b):
    """Adds two numbers and returns the sum."""
    return a + b

def subtract(a, b):
    """Subtracts the second number from the first and returns the difference."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers and returns the product."""
    return a * b

def divide(a, b):
    """Divides the first number by the second and returns the quotient.
    Raises ValueError if the second number is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Raises the first number to the power of the second number."""
    return a ** b

def modulo(a, b):
    """Returns the remainder of the division of the first number by the second."""
    if b == 0:
        raise ValueError("Cannot perform modulo with zero divisor")
    return a % b