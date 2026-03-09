"""
Name: Ishan Agarwal
Date: March 8th, 2026
Purpose: This program uses another function to print results.
"""

import temp_converter as tc

def main() -> None:
    """
    This is the orchestrator function. 
    It takes the user input and then uses a imported functions to perform its conversion.
    """

    temp_celsius: float = float(input("Enter temperature in Celsius: "))
    temp_fahrenheit: float = tc.temp_convert(temp_celsius)
    tc.result(temp_celsius, temp_fahrenheit)

if __name__ == "__main__":
    main()