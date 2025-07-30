#Robust Division Calculator with Command Line Arguments

import sys
def robust_divide(numerator, denominator):
    """Perform division with error handling."""
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both numerator and denominator must be numbers."

def safe_divide(numerator, denominator):
    """Wrapper function to handle command line arguments."""
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Both numerator and denominator must be numeric values."

    return robust_divide(num, denom)


import sys
from robust_division_calculator import safe_divide    
def main():    
    """Main function to handle command line arguments."""
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)

    print(f"Result: {result}")