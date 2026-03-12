#Program to write 3 names in a file

list_of_names = ['bob', 'daniel', 'farhan']
physics_marks = [60, 70, 80]
fp = open('names.txt', 'a')

for i in range(len(list_of_names)):
    student_record = list_of_names[i] + ', ' + str(physics_marks[i] ) 
    fp.write(student_record)
    fp.write('\n')

fp.close()
