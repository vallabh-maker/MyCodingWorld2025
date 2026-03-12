#Program to find the sum of even numbers and product of odd numbers from 1 to n.

i = 1
n = int(input("Enter n: "))
summ = 0
product = 1
while i <= n:
    if i%2 == 0:
        summ += i
        i += 1
    else:
        product *= i
        i += 1
print(f"The sum of even numbers till {n} is {summ} and the product of odd numbers till {n} is {product}")
        
