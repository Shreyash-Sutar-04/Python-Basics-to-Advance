# Temprature converter 
unit = input("Unit for measurement Fahrenheit or Celsius? F/C: ")
measurement = float(input("Enter the measurement: "))

if unit.upper() == "F":
    # Correct formula for Fahrenheit to Celsius
    celsius = (measurement - 32) * 5/9
    print(f"The temperature in Celsius is: {celsius}")
elif unit.upper() == "C":
    # Correct formula for Celsius to Fahrenheit
    fahrenheit = (measurement * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit}")
else:
    print("Invalid unit provided")

#The .upper() method was added to the unit variable to handle user input like "f" or "c" 
# without an error, making the program more user-friendly.