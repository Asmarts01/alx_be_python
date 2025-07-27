#Temperature conversion tool
# This module provides functions to convert temperatures between Celsius and Fahrenheit.
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9  
def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32 

def convert_temperature():
    """Prompt user for temperature and convert it."""
    temp = float(input("Enter the temperature: "))
    unit = input("Is this in Celsius (C) or Fahrenheit (F)? ").strip().upper()
    
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp:.2f}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
        