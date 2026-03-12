#Define a function to find the sum of two numbers


def find_sum():
    a = float(input("Input first number - "))
    b = float(input("Input second number - "))
    summ = a + b
    print(f'The sum of {a} and {b} is {summ}')

def find_difference():
    a = float(input("Input first number - "))
    b = float(input("Input second number - "))
    diff = a - b
    print(f'The difference between {a} and {b} is {diff}')



def calculator_menu():
    print("--------------------------------------------------")
    print("                 Calculator                       ")
    print("--------------------------------------------------")
    print("                1. Addition                       ")
    print("--------------------------------------------------")
    print("                2. Subtraction                    ")
    print("--------------------------------------------------")

    choice = int(input("Choose the operation you wish to perform "))

    if choice == 1:
        find_sum()
    elif choice == 2:
        find_difference()
    else:
        print("Invalid input")


#MAIN
calculator_menu()



