#Create 2 lists
list_of_names = [ 'rohan', 'bob', 'ram', 'john', 'jack']
physics_marks = [50, 70, 60, 40, 80]
chemistry_marks = [80, 60, 30, 90, 40]
math_marks = [70, 40, 60, 50, 80]
comp_marks = [60, 50, 80, 40, 70]

#Display the original data

total_p = 0
total_c = 0
total_m = 0
total_cs = 0
total = 0
print('-----------------------------------------------------------------------------------------------')
print('| NAME        |   PHYSICS     |   CHEMISTRY   |      MATH     |  COMPUTER SC  |     TOTAL     |')
print('-----------------------------------------------------------------------------------------------')
for i in range(len(list_of_names)):
    name = list_of_names[i]
    p = physics_marks[i]
    c = chemistry_marks[i]
    m = math_marks[i]
    cs = comp_marks[i]
    total_p +=p
    total_c +=c
    total_m +=m
    total_cs +=cs
    total = p + c + m + cs
    print(f'| {name:11} | {p:>13} | {c:>13} | {m:>13} | {cs:>13} | {total:>13} |')
    total = 0
print('-----------------------------------------------------------------------------------------------')
print(f'| class total | {total_p:>13} | {total_c:>13} | {total_m:>13} | {total_cs:>13} |               ')
print('-----------------------------------------------------------------------------------------------')
#Sort the data

for i in range(len(list_of_names) - 1):
    for j in range(len(list_of_names) - 1 - i):
        if list_of_names[j] > list_of_names[j + 1]:
            temp1 = list_of_names[j]
            list_of_names[j] = list_of_names[j + 1]
            list_of_names[j + 1] = temp1
            temp2 = physics_marks[j]
            physics_marks[j] = physics_marks[j + 1]
            physics_marks[j + 1] = temp2
            temp3 = chemistry_marks[j]
            chemistry_marks[j] = chemistry_marks[j + 1]
            chemistry_marks[j + 1] = temp3
            temp4 = math_marks[j]
            math_marks[j] = math_marks[j + 1]
            math_marks[j + 1] = temp4
            temp5 = comp_marks[j]
            comp_marks[j] = comp_marks[j + 1]
            comp_marks[j + 1] = temp5

#Display the sorted data
total_p = 0
total_c = 0
total_m = 0
total_cs = 0
total = 0
print('-----------------------------------------------------------------------------------------------')
print('| NAME        |   PHYSICS     |   CHEMISTRY   |      MATH     |  COMPUTER SC  |     TOTAL     |')
print('-----------------------------------------------------------------------------------------------')
for i in range(len(list_of_names)):
    name = list_of_names[i]
    p = physics_marks[i]
    c = chemistry_marks[i]
    m = math_marks[i]
    cs = comp_marks[i]
    total_p +=p
    total_c +=c
    total_m +=m
    total_cs +=cs
    total = p + m + c + cs
    print(f'| {name:11} | {p:>13} | {c:>13} | {m:>13} | {cs:>13} | {total:>13} |')
    total = 0
print('-----------------------------------------------------------------------------------------------')
print(f'| class total | {total_p:>13} | {total_c:>13} | {total_m:>13} | {total_cs:>13} |               |')
print('-----------------------------------------------------------------------------------------------')
