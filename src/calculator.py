# src/calculator.py

def add(a: float, b: float) -> float:
    """
    Performs addition of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Performs subtraction of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The difference between a and b.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Performs multiplication of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Performs division of two numbers.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The quotient of a divided by b.

    Raises:
        ValueError: If the denominator b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"10 / 2 = {divide(10, 2)}")
    try:
        print(f"7 / 0 = {divide(7, 0)}")
    except ValueError as e:
        print(f"Error: {e}")