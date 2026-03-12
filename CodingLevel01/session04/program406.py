'''
Program to print the following pattern

# # # # # #
$ $ $ $ $ $
# # # # # #
$ $ $ $ $ $
'''

i = 1
k = 1
while i <= 4:
    j = 1
    while j <= 6:
        if k%2 == 1:
            print('#', end = " ")
        else:
            print('$', end = " ")
        j += 1
    k += 1    
    print()
    i += 1
