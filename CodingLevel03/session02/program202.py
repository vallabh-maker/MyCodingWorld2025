import tkinter as tk 

root_window = tk.Tk()

students = {}

rollno = 1

def store():
    global rollno
    name = entry_name.get()
    marks_p = float(entry_p.get())
    marks_c = float(entry_c.get())
    marks_m = float(entry_m.get())
    marks_cs = float(entry_cs.get())
    value = (name, marks_p, marks_c, marks_m, marks_cs)
    students[rollno] = value
    rollno +=1
    label_rollno.configure(text = f'Roll number {rollno}')
    entry_name.delete(0, tk.END)
    entry_p.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    entry_m.delete(0, tk.END)
    entry_cs.delete(0, tk.END)
def display():
    all_students = ''
    header = f"| {'Name':^15} | {'Phy':^6} | {'Chem':^6} | {'Math':^6} | {'CS':^6} | {'Avg':^6} |"
    for i in range(len(header)):
        all_students += '-'
    all_students += '\n'
    all_students += header
    all_students += '\n'
    for i in range(len(header)):
        all_students += '-'
    all_students += '\n'
    total_p = 0
    total_c = 0
    total_m = 0
    total_cs = 0
    for key in students:
        value = students[key]
        name = value[0] 
        marks_p = value[1]
        marks_c = value[2]
        marks_m = value[3]
        marks_cs = value[4]
        avg = (marks_p + marks_c + marks_m + marks_cs)/4
        total_p += marks_p
        total_c += marks_c
        total_m += marks_m
        total_cs += marks_cs
        student_record = f'| {name:^15} | {marks_p:^6} |{marks_c:^6} | {marks_m:^6} | {marks_cs:^6} | {avg:^6} |'
        all_students += student_record + '\n'
    totals = f'| {'total':^6} | {total_p:^6} | {total_c:^6} | {total_m:^6} | {total_cs:^6} |          |'
    all_students += totals
    all_students += '\n'
    for i in range(len(header)):
        all_students += '-'
    result.configure(text = all_students)
    
    
        

label_rollno = tk.Label(root_window, text = f'Roll number {rollno}')
label_name = tk.Label(root_window, text = 'Enter the name of student')
entry_name = tk.Entry(root_window)
label_p = tk.Label(root_window, text = 'Enter the physics marks of student')
entry_p = tk.Entry(root_window)
label_c = tk.Label(root_window, text = 'Enter the chemistry marks of student')
entry_c = tk.Entry(root_window)
label_m = tk.Label(root_window, text = 'Enter the math marks of student')
entry_m = tk.Entry(root_window)
label_cs = tk.Label(root_window, text = 'Enter the computer science marks of student')
entry_cs = tk.Entry(root_window)
save = tk.Button(root_window, text = 'Save details of student', command = store)
display_all = tk.Button(root_window, text = 'Display all', command = display)
result = tk.Label(root_window, text = '', font = ('Courier new', 12))
label_rollno.grid(row = 0, columnspan = 2)
label_name.grid(row = 1, column = 0)
entry_name.grid(row = 1, column = 1)
label_p.grid(row = 2, column = 0)
entry_p.grid(row = 2, column = 1)
label_c.grid(row = 3, column = 0)
entry_c.grid(row = 3, column = 1)
label_m.grid(row = 4, column = 0)
entry_m.grid(row = 4, column = 1)
label_cs.grid(row = 5, column = 0)
entry_cs.grid(row = 5, column = 1)
save.grid(row = 6, column = 0)
display_all.grid(row = 6, column = 1)
result.grid(row = 7, columnspan = 2)

root_window.mainloop()  