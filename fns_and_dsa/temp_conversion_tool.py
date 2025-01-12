FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32

temperature_value=int(input("Enter the temperature to convert: "))
temperature_choice=input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if temperature_choice=="F":
    fahrenheit=temperature_value
    result=convert_to_celsius(fahrenheit)
    print(str(fahrenheit)+"°F is "+str(result)+"°C")


elif temperature_choice=="C":
    celsius=temperature_value
    result=convert_to_fahrenheit(celsius)
    print(str(celsius)+"°C is "+str(result)+"°F")

    
else:
    print("Invalid temperature. Please enter a numeric value. ")