#To arrange the values in a list in ascending order

a = [30, 50, 20, 10, 40]

for i in range(len(a) - 1):
    for j in range(len(a) - 1 - i):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

for i in range(len(a)):
    num = a[i]
    print(num)
