#To make a menu driven program to check if a number is even or odd and if a number is positive or negative

def check_if_number_is_odd_or_even():
    number = float(input('Input the number '))
    if number%2 == 0:
        print(f'{number} is an even number')
    else:
        print(f'{number} is an odd number')

def check_if_number_is_positive_or_negative():
    number = float(input('Input the number '))
    if number > 0:
        print(f'{number} is positive')
    elif number < 0:
        print(f'{number} is negative')
    else:
        print('The input number is 0')

def menu():
    print("--------------------------------------------------")
    print("                     Checks                       ")
    print("--------------------------------------------------")
    print("                 1. Odd or even                   ")
    print("--------------------------------------------------")
    print("            2. Positive or negative               ")
    print("--------------------------------------------------")

    choice = int(input("Choose the check you wish to perform "))

    if choice == 1:
        check_if_number_is_odd_or_even()
    elif choice == 2:
        check_if_number_is_positive_or_negative()
    else:
        print("Invalid input")
menu()
