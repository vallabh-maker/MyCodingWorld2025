'''
4. Menu driven program to perform the following
 	a) Print numbers from 1 to n
b) Print even numbers from 1 to n
c) Print odd numbers from 1 to n
d) Print numbers from n to 1
'''

def print_numbers_from_1_to_n():
    n = int(input('Input n'))
    k = 1
    while k <= n:
        print(k)
        k += 1

def print_even_numbers_from_1_to_n():
    n = int(input('Input n'))
    k = 1
    while k <= n and k%2 == 0:
        print(k)
        k += 1

def print_odd_numbers_from_1_to_n():
    n = int(input('Input n'))
    k = 1
    while k <= n:
        print(k)
        k += 2

def print_numbers_from_n_to_1():
    n = int(input('Input n'))
    k = n
    while k >= 1:
        print(k)
        k -= 1

def menu():
    print("--------------------------------------------------")
    print("              Printing numbers                    ")
    print("--------------------------------------------------")
    print("              1. From 1 to n                      ")
    print("--------------------------------------------------")
    print("             2. Even from 1 to n                  ")
    print("--------------------------------------------------")
    print("              3. Odd from 1 to n                  ")
    print("--------------------------------------------------")
    print("             4. From n to 1                       ")
    print("--------------------------------------------------")

    choice = int(input("Choose the form of interest you wish to calculate "))

    if choice == 1:
        print_numbers_from_1_to_n()
    elif choice == 2:
        print_even_numbers_from_1_to_n()
    elif choice == 3:
        print_odd_numbers_from_1_to_n()
    elif choice == 4:
        print_numbers_from_n_to_1()
    else:
        print("Invalid input")

menu()
