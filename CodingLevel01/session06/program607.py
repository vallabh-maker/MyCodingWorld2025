#Program to find simple interest and compound interest

def calculate_SI():
    p = float(input('Input the principle amount'))
    r = float(input('Input the interest rate'))
    t = float(input('Input the time in years'))
    SI = (p*r*t)/100
    print(f'The simple interest on a principle of {p} at rate {r}% over {t} years is {SI}')

def calculate_CI():
    p = float(input('Input the principle amount'))
    r = float(input('Input the interest rate'))
    t = float(input('Input the time in years'))
    A = p*(1 + r/100)^t
    CI = A - p
    print(f'The compound interest on a principle of {p} at rate {r}% over {t} years is {SI}')
    
def menu():
    print("--------------------------------------------------")
    print("              Interest Calculation                ")
    print("--------------------------------------------------")
    print("              1. Simple Interest                  ")
    print("--------------------------------------------------")
    print("             2. Compound Interest                 ")
    print("--------------------------------------------------")

    choice = int(input("Choose the form of interest you wish to calculate "))

    if choice == 1:
        calculate_SI()
    elif choice == 2:
        calculate_CI()
    else:
        print("Invalid input")
menu()
