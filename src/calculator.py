# src/calculator.py

def add(x, y):
    """Adds two numbers and returns the sum."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers and returns the difference."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers and returns the product."""
    return x * y

def divide(x, y):
    """Divides two numbers and returns the quotient.
    Handles division by zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def main():
    """Demonstrates basic calculator operations."""
    print("Simple Calculator Operations:")
    
    num1 = 10
    num2 = 5

    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    
    try:
        print(f"{num1} / {num2} = {divide(num1, num2)}")
        print(f"{num1} / 0 = {divide(num1, 0)}") # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()