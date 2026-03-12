'''
5. Menu driven program to perform the following
a) Sum of numbers from 1 to n
b) Sum of even numbers from 1 to n
c) Sum of odd numbers from 1 to n
'''

def print_sum_from_1_to_n():
    n = int(input('Input n'))
    k = 1
    summm = 1
    while k <= n:
        summ = summ + k
        k += 1
    print(summ)

def print_sum_of_even_from_1_to_n():
    n = int(input('Input n'))
    k = 2
    summm = 1
    while k <= n:
        summ = summ + k
        k += 2
    print(summ)

def print_sum_of_odd_from_1_to_n():
n = int(input('Input n'))
    k = 1
    summm = 1
    while k <= n:
        summ = summ + k
        k += 2
    print(summ)

def menu():
    print("--------------------------------------------------")
    print("              Sum of numbers                      ")
    print("--------------------------------------------------")
    print("              1. From 1 to n                      ")
    print("--------------------------------------------------")
    print("             2. Even from 1 to n                  ")
    print("--------------------------------------------------")
    print("              3. Odd from 1 to n                  ")
    print("--------------------------------------------------")

    choice = int(input("Choose the form of interest you wish to calculate "))

    if choice == 1:
        print_sum_from_1_to_n()
    elif choice == 2:
        print_sum_of_even_from_1_to_n()
    elif choice == 3:
        print_sum_of_odd_from_1_to_n()
    else:
        print('Invalid input')

menu()
