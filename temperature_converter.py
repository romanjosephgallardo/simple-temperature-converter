# Temperature Converter

#  Ask the user to input a temperature
temperature = float(input(f"Temperature Converter --- \n"
                          f"Enter temperature: "))
#  Ask user to select conversion type
conversion_type = int(input(f"Conversion Type --- \n"
                            f"1. Celsius to Fahrenheit \n"
                            f"2. Fahrenheit to Celsius \n"))

#  Computation for Celsius to Fahrenheit
if conversion_type == 1:
    celsius_to_fahrenheit = (temperature * 9/5) + 32
    print(f"Temperature in Celsius: {temperature}C°")
    print(f"Temperature to Fahrenheit: {celsius_to_fahrenheit:.3g}F°")

#  Computation for Fahrenheit to Celsius
elif conversion_type == 2:
    celsius_to_fahrenheit = (temperature - 32) * 5/9
    print(f"Temperature in Fahrenheit: {temperature}F°")
    print(f"Temperature to Celsius: {celsius_to_fahrenheit:.3g}C°")
    
else:
    print("Invalid Conversion Type")
