#program for temperature conversions using functions
def convert_fahrenheit_to_celsius():
    fahrenheit = float(input('Input the temperature in fahrenheit  - '))
    celsius = (fahrenheit - 32)*5/9
    print(f'The temperature in celsius if the temperature in fahrenheit is {fahrenheit} is {celsius}')

def convert_celsius_to_fahrenheit():
    celsius = float(input('Input the temperature in celsius - '))
    fahrenheit = celsius*9/5 + 32
    print(f'The temperature in fahrenheit if the temperature in celsius is {celsius} is {fahrenheit}')

def menu():
    print("--------------------------------------------------")
    print("                 Conversions                      ")
    print("--------------------------------------------------")
    print("           1. Fahrenheit to Celsius               ")
    print("--------------------------------------------------")
    print("           2. Celsius to Fahrenheit               ")
    print("--------------------------------------------------")

    choice = int(input("Choose the conversion you wish to perform "))

    if choice == 1:
        convert_fahrenheit_to_celsius()
    elif choice == 2:
        convert_celsius_to_fahrenheit()
    else:
        print("Invalid input")
menu()
    
