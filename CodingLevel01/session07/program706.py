#Define a funtcion to accept n as a parameter and display its factors

def display_factors(n):
    k = 1
    counter = 0
    while k <= n:
        if n%k == 0:
            counter += 1
        k += 1
    if counter == 2:
        return True
    else:
        return False

#MAIN
x = 18
result = display_factors(x)
if result == True:
    print(f'{x} is a prime number')
else:
    print(f'{x} is a composite number')



