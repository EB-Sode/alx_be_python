
FAHRENHEIT_TO_CELSIUS_FACTOR =  5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =  9/5

def convert_to_celcius (fahrenheit):
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result

def convert_to_fahrenheit(celcius):
    result = (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return result

temperature= float(input("Enter the temperature to convert: "))
degree = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
try:
    if degree == "c":
        temp = convert_to_fahrenheit(temperature)
        print (f"{temperature}°C is {temp}°F")
    elif degree == "f":
        temp = convert_to_celcius(temperature)
        print(f"{temperature}°F is {temp}°C ")
    else:
        print("invalid input")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")