# This task aims to illustrate when and how to use @classmethod and @staticmethod decorators, highlighting their differences and practical applications.
class Calculator:

    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Returns the product of two numbers using the class name."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    