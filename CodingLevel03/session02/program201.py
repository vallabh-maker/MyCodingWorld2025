import tkinter as tk
root_window = tk.Tk()

root_window.title('List of marks and students')

list_of_marks = []
list_of_names = []

def add_student():
    name = entryName.get()
    marks = entryMarks.get()
    list_of_names.append(name)
    list_of_marks.append(marks)
    
def display_all():
    all_students = "|       name       |  marks  |" + '\n'
    for i in range(len(list_of_marks)):
        name = list_of_names[i]
        marks = list_of_marks[i]
        student_record = f'| {name:^16} | {marks:^6} |'
        all_students += student_record+ "\n"
    labelAll.configure(text = all_students)
    

labelHeading = tk.Label(root_window, text = 'Marks Sheet')

labelName = tk.Label(root_window, text = "Enter student's name") 
entryName = tk.Entry(root_window)

labelMarks = tk.Label(root_window, text = "Enter student's marks")
entryMarks = tk.Entry(root_window)

button_Add_student = tk.Button(root_window, text = 'Add student', command = add_student)

button_display_all = tk.Button(root_window, text = 'Display all', command = display_all)
labelAll = tk.Label(root_window, text = '', font=('Courier', 12, 'bold'))

labelHeading.grid(row = 0, columnspan = 2)

labelName.grid(row = 1, column = 0)
entryName.grid(row = 1, column = 1)

labelMarks.grid(row = 2, column = 0)
entryMarks.grid(row = 2, column = 1)

button_Add_student.grid(row = 3, column = 0)
button_display_all.grid(row = 3, column = 1)

labelAll.grid(row = 4)

root_window.mainloop()