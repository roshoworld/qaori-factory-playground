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
    """Return a divided by b.

    Raises:
        ValueError: If the divisor b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b