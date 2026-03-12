#Program to define a fucntion to accept principle, time and rate and return the simple interest

def find_interest(p,r,t):
    S_I = (p*r*t)/100
    return S_I
x = 10000
y = 7
z = 3

result = find_interest(x,y,z)
print(f'The simple interest on a sum of ruppees {x} at a rate of {y}% over {z} years is {result}')
