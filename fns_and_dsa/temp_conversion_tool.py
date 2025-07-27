#Temperature conversion tool
# This module provides functions to convert temperatures between Celsius and Fahrenheit.

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    :param celsius: Temperature in Celsius.
    :return: Temperature in Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius.
    :param fahrenheit: Temperature in Fahrenheit.
    :return: Temperature in Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_temperature():
    """
    Convert temperature between Celsius and Fahrenheit based on user input.
    """
    temp_value = float(input("Enter the temperature to convert:"))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()
    if unit == 'C':
        converted_temp = celsius_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted_temp:.2f}°F")
    elif unit == 'F':
        converted_temp = fahrenheit_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted_temp:.2f}°C")
    else:
        print("Invalid temperature. Please enter a numeric value.")
    
if __name__ == "__main__":
    convert_temperature()
