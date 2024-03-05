class Calculator:
    def __init__(self):
        """Constructor method that initializes the Calculator instance."""
        pass

    def sum(self, a, b):
        """Method to add two numbers."""
        return a + b

    def difference(self, a, b):
        """Method to subtract one number from another."""
        return a - b

    def product(self, a, b):
        """Method to multiply two numbers."""
        return a * b

    def quotient(self, a, b):
        """Method to divide one number by another."""
        if b == 0:
            # Check if the divisor is zero to avoid division by zero.
            raise ValueError("Error, zero division!")
        return a / b
