import logging

# Configure logging for the calculator module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# Add a handler if not already configured by the main application
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def add(a: float, b: float) -> float:
    """Adds two numbers and returns the sum."""
    logger.info(f"Adding {a} and {b}")
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first and returns the result."""
    logger.info(f"Subtracting {b} from {a}")
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiplies two numbers and returns the product."""
    logger.info(f"Multiplying {a} by {b}")
    return a * b

def divide(a: float, b: float) -> float:
    """Divides the first number by the second and returns the quotient.
    Raises ValueError if division by zero is attempted.
    """
    logger.info(f"Dividing {a} by {b}")
    if b == 0:
        logger.error("Attempted to divide by zero")
        raise ValueError("Cannot divide by zero")
    return a / b