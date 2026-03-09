"""
Name: Ishan Agarwal
Date: March 8th, 2026
Purpose: This program has two functions. 
- Function 1: Convert the temperature to a different unit
- Function 2: Print the result
"""


def temp_convert(temp_celsius: float) -> float:
    """
    This is the task-based function. This converts the temperature from Celsius to Fahrenheit.
    It takes one parameter: temp_celsius, which is of type float
    It returns the converted temp.
    """

    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit


def result(temp_celsius: float, temp_fahrenheit: float) -> None:
    """
    This is the side-effect function. This prints the result of the conversion.
    It takes two parameter: temp_celsius & temp_fahrenheit, both of which are of type float
    It returns nothing.
    """
    
    print(f"{temp_celsius} degrees Celsius is equal to {temp_fahrenheit} degrees Fahrenheit.")

