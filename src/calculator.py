class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        # Bug: No error handling for division by zero
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    print(f"1 + 1 = {calc.add(1, 1)}")
