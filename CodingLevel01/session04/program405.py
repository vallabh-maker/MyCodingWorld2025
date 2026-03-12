'''
Program to print the following pattern

# * # * # *
# * # * # *
# * # * # *
'''

i = 1

while i <= 3:
    j = 1
    while j <= 6:
        if j%2 == 1:
            print('#', end = " ")
        else:
            print('*', end = " ")
        j += 1
    print()
    i += 1
