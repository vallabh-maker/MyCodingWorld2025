'''
Program to print the following pattern

1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
'''

i = 1
while i <= 3:
    j = 1
    while j <= 5:
        print(i, end = " ")
        j += 1
    print()
    i += 1
