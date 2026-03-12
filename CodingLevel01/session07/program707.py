#Write a program to calculate primorial of a given number

def calculate_primorial(n):
    k = 1
    primorial = 1
    while k <= n:
        m = 1
        counter = 0
        while m <= k:
            if k%m == 0:
                counter += 1
            m += 1
        if counter == 2:
            primorial = primorial*k
        k += 1
    return primorial

x = 25
result = calculate_primorial(x)
print(f'The primorial of {x} is {result}')
                
