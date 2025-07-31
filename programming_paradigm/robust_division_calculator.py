#Robust Division Calculator with Command Line Arguments

import sys
def robust_divide(numerator, denominator):
    """Perform division with error handling."""
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Please enter numeric values only."

def safe_divide(numerator, denominator):
    """Wrapper function to handle command line arguments."""
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

    