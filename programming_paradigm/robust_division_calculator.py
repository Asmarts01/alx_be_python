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
    except ValueError:
        return "Error: Please enter numeric values only."

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

    print(f"The result of the division is {result}")