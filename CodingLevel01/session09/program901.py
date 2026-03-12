#Create 2 lists
list_of_names = ['bob', 'john', 'jack', 'ram', 'rohan']
list_of_marks = [40, 50, 60, 70, 80, 90]

#Add items
list_of_names.append('james')
list_of_marks.append(30)

#Display the list
total = 0
print('-----------------------')
print('| NAME        | MARKS |')
print('-----------------------')
for i in range(len(list_of_names)):
    name = list_of_names[i]
    marks = list_of_marks[i]
    print(f'| {name:11} | {marks:>5} |')
    total += marks
print('-----------------------')
print(f'| class total | {total:>5} |')
print('-----------------------')

