
# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt the user to enter a temperature
        temp = int(input("Enter the temperature to convert: "))
        # Ask the user for the scale
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()
        
        if scale == "C":
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is equivalent to {converted_temp:}°F.")
        elif scale == "F":
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is equivalent to {converted_temp:}°C.")
        else:
            # Handle invalid scale input
            print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        # Handle invalid temperature input
        print("Invalid temperature. Please enter a numeric value.")

# Run the program
if __name__ == "__main__":
    main()

