class Calculator:
    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Subtract one number from another."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Divide one number by another.
        
        Returns positive infinity if division by zero occurs.
        """
        return a / b if b != 0 else float('inf')

