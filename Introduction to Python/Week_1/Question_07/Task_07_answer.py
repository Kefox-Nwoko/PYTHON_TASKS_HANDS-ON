#user input of temp in celcius
celcius = int(input("Enter temperature in Celcius: "))
# using formula to convert celcius to farenheit
fahrenheit = format(((celcius *(9/5)) + 32),".2f")
# printing output
print(f'{celcius} Celcius = {fahrenheit} Fahrenheit')