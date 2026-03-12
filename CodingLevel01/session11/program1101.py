fp = open('students.txt', 'r')

list_of_records = fp.readlines()

print('-------------------------------------------------------------------------------------')
print('|   Name    |  Physics  | Chemistry |   Maths   | Computer  |   Total   |  Average  |')
print('-------------------------------------------------------------------------------------')
list_of_names = []
physics_marks = []
chemistry_marks = []
math_marks = []
comp_marks = []
list_of_totals = []
list_of_averages = []
total_p = 0
total_c = 0
total_m = 0
total_cs = 0
for i in range(1, len(list_of_records)):
    student_record = list_of_records[i]
    student_record = student_record.strip()
    list_of_tokens = student_record.split(',')
    name = list_of_tokens[0]
    marks_p = int(list_of_tokens[1])
    marks_c = int(list_of_tokens[2])
    marks_m = int(list_of_tokens[3])
    marks_cs = int(list_of_tokens[4])
    total = marks_p + marks_c + marks_m + marks_cs
    avg = total/4
    list_of_names.append(name)
    physics_marks.append(marks_p)
    chemistry_marks.append(marks_c)
    math_marks.append(marks_m)
    comp_marks.append(marks_cs)
    list_of_totals.append(total)
    list_of_averages.append(avg)
    total_p += marks_p
    total_c += marks_c
    total_m += marks_m
    total_cs += marks_cs
    print(f'| {name:^9} | {marks_p:^9} | {marks_c:^9} | {marks_m:^9} | {marks_cs:^9} | {total:^9} | {avg:^9} |')
    
print('-------------------------------------------------------------------------------------')
print(f'|   Total   | {total_p:^9} | {total_c:^9} | {total_m:^9} | {total_cs:^9} |           |           |')
print('-------------------------------------------------------------------------------------')

def sort_names_ascending():
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
    for i in range(len(list_of_names)):
        name = list_of_names[i]
        marks_p = physics_marks[i]
        marks_c = chemistry_marks[i]
        marks_m = math_marks[i]
        marks_cs = comp_marks[i]
        total = marks_p + marks_c + marks_m + marks_cs
        avg = total/4
        print(f'| {name:^9} | {marks_p:^9} | {marks_c:^9} | {marks_m:^9} | {marks_cs:^9} | {total:^9} | {avg:^9} |')
    print('-------------------------------------------------------------------------------------')
    print(f'|   Total   | {total_p:^9} | {total_c:^9} | {total_m:^9} | {total_cs:^9} |           |           |')
    print('-------------------------------------------------------------------------------------')
    
def sort_names_descending():
    for i in range(len(list_of_names) - 1):
        for j in range(len(list_of_names) - 1 - i):
            if list_of_names[j] < list_of_names[j + 1]:
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
    for i in range(len(list_of_names)):
        name = list_of_names[i]
        marks_p = physics_marks[i]
        marks_c = chemistry_marks[i]
        marks_m = math_marks[i]
        marks_cs = comp_marks[i]
        total = marks_p + marks_c + marks_m + marks_cs
        avg = total/4
        print(f'| {name:^9} | {marks_p:^9} | {marks_c:^9} | {marks_m:^9} | {marks_cs:^9} | {total:^9} | {avg:^9} |')
    print('-------------------------------------------------------------------------------------') 
    print(f'|   Total   | {total_p:^9} | {total_c:^9} | {total_m:^9} | {total_cs:^9} |           |           |')
    print('-------------------------------------------------------------------------------------')
def sort_totals_ascending():
    for i in range(len(list_of_names) - 1):
        for j in range(len(list_of_names) - 1 - i):
            if list_of_totals[j] > list_of_totals[j + 1]:
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
                temp6 = list_of_totals[j]
                list_of_totals[j] = list_of_totals[j + 1]
                list_of_totals[j + 1] = temp6
    for i in range(len(list_of_names)):
        name = list_of_names[i]
        marks_p = physics_marks[i]
        marks_c = chemistry_marks[i]
        marks_m = math_marks[i]
        marks_cs = comp_marks[i]
        total = marks_p + marks_c + marks_m + marks_cs
        avg = total/4
        print(f'| {name:^9} | {marks_p:^9} | {marks_c:^9} | {marks_m:^9} | {marks_cs:^9} | {total:^9} | {avg:^9} |')
    print('-------------------------------------------------------------------------------------')
    print(f'|   Total   | {total_p:^9} | {total_c:^9} | {total_m:^9} | {total_cs:^9} |           |           |')
    print('-------------------------------------------------------------------------------------')

def sort_totals_descending():
    for i in range(len(list_of_names) - 1):
        for j in range(len(list_of_names) - 1 - i):
            if list_of_totals[j] < list_of_totals[j + 1]:
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
                temp6 = list_of_totals[j]
                list_of_totals[j] = list_of_totals[j + 1]
                list_of_totals[j + 1] = temp6
    for i in range(len(list_of_names)):
        name = list_of_names[i]
        marks_p = physics_marks[i]
        marks_c = chemistry_marks[i]
        marks_m = math_marks[i]
        marks_cs = comp_marks[i]
        total = marks_p + marks_c + marks_m + marks_cs
        avg = total/4
        print(f'| {name:^9} | {marks_p:^9} | {marks_c:^9} | {marks_m:^9} | {marks_cs:^9} | {total:^9} | {avg:^9} |')
    print('-------------------------------------------------------------------------------------')
    print(f'|   Total   | {total_p:^9} | {total_c:^9} | {total_m:^9} | {total_cs:^9} |           |           |')
    print('-------------------------------------------------------------------------------------')

def sort_averages_ascending():
    for i in range(len(list_of_names) - 1):
        for j in range(len(list_of_names) - 1 - i):
            if list_of_averages[j] > list_of_averages[j + 1]:
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
                temp6 = list_of_totals[j]
                list_of_totals[j] = list_of_totals[j + 1]
                list_of_totals[j + 1] = temp6
                temp7 = list_of_averages[j]
                list_of_averages[j] = list_of_averages[j + 1]
                list_of_averages[j + 1] = temp7
    for i in range(len(list_of_names)):
        name = list_of_names[i]
        marks_p = physics_marks[i]
        marks_c = chemistry_marks[i]
        marks_m = math_marks[i]
        marks_cs = comp_marks[i]
        total = marks_p + marks_c + marks_m + marks_cs
        avg = total/4
        print(f'| {name:^9} | {marks_p:^9} | {marks_c:^9} | {marks_m:^9} | {marks_cs:^9} | {total:^9} | {avg:^9} |')
    print('-------------------------------------------------------------------------------------')
    print(f'|   Total   | {total_p:^9} | {total_c:^9} | {total_m:^9} | {total_cs:^9} |           |           |')
    print('-------------------------------------------------------------------------------------')

def sort_averages_descending():
    for i in range(len(list_of_names) - 1):
        for j in range(len(list_of_names) - 1 - i):
            if list_of_averages[j] < list_of_averages[j + 1]:
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
                temp6 = list_of_totals[j]
                list_of_totals[j] = list_of_totals[j + 1]
                list_of_totals[j + 1] = temp6
                temp7 = list_of_averages[j]
                list_of_averages[j] = list_of_averages[j + 1]
                list_of_averages[j + 1] = temp7
    for i in range(len(list_of_names)):
        name = list_of_names[i]
        marks_p = physics_marks[i]
        marks_c = chemistry_marks[i]
        marks_m = math_marks[i]
        marks_cs = comp_marks[i]
        total = marks_p + marks_c + marks_m + marks_cs
        avg = total/4
        print(f'| {name:^9} | {marks_p:^9} | {marks_c:^9} | {marks_m:^9} | {marks_cs:^9} | {total:^9} | {avg:^9} |')
    print('-------------------------------------------------------------------------------------')
    print(f'|   Total   | {total_p:^9} | {total_c:^9} | {total_m:^9} | {total_cs:^9} |           |           |')
    print('-------------------------------------------------------------------------------------')
    
def menu():
    print('-------------------------------------------------------------------------------------')    
    print('                                      MENU                                           ')
    print('-------------------------------------------------------------------------------------')
    print('                         1. Sort by names in ascending order                         ')
    print('-------------------------------------------------------------------------------------')
    print('                         2. Sort by names in descending order                        ')
    print('-------------------------------------------------------------------------------------')
    print('                       3. Sort by total marks in ascending order                     ')
    print('-------------------------------------------------------------------------------------')
    print('                       4. Sort by total marks in descending order                    ')
    print('-------------------------------------------------------------------------------------')
    print('                       5. Sort by average marks in ascending order                   ')
    print('-------------------------------------------------------------------------------------')
    print('                       6. Sort by average marks in ascending order                   ')
    print('-------------------------------------------------------------------------------------')
    choice = int(input('Input the type of sorting: '))
    print('-------------------------------------------------------------------------------------')
    print('|   Name    |  Physics  | Chemistry |   Maths   | Computer  |   Total   |  Average  |')
    print('-------------------------------------------------------------------------------------')
    if choice == 1:
        sort_names_ascending()
    elif choice == 2:
        sort_names_descending()
    elif choice == 3:
        sort_totals_ascending()
    elif choice == 4:
        sort_totals_descending()
    elif choice == 5:
        sort_averages_ascending()
    elif choice == 6:
        sort_averages_descending()
    else:
        print('Invalid Choice')
menu()


