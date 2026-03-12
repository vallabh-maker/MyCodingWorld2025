import pymysql as bot
import tkinter as tk
connection = bot.connect(
    host = "localhost",
    user = "root",
    password = "Tiger@123",
    database = "school"
    )
cursor = connection.cursor()



def entering():
    query_entry = 'INSERT INTO marksheet(rollno, name, marks, grade, section) VALUES(%s, %s, %s, %s, %s)'
    rollno = entry_rollno.get()
    name = entry_name.get()
    marks = entry_marks.get()
    grade = entry_grade.get()
    section = entry_section.get()
    values = (rollno, name, marks, grade, section)
    cursor.execute(query_entry, values)
    entry_rollno.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_marks.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    entry_section.delete(0, tk.END)
    connection.commit()

def showing():
    query_showing = 'SELECT * FROM marksheet'
    cursor.execute(query_showing)
    list_of_rows = cursor.fetchall()
    roll_no = 'Roll no.'
    student_name = 'Name'
    student_marks = 'Marks'
    student_grade = 'Grade'
    student_section = 'Section'
    msg = ''
    msg += '------------------------------------------------------------------------------' + '\n'
    msg += f'| {roll_no:10} | {student_name:15} | {student_marks:6} | {student_grade:4} | {student_section:3} |' + '\n'
    msg += '------------------------------------------------------------------------------' + '\n'
    for record in list_of_rows:
        roll_no = record[0]
        student_name = record[1]
        student_marks = record[2]
        student_grade = record[3]
        student_section = record[4]
        msg += f'| {roll_no:4} | {student_name:15} | {student_marks:6} | {student_grade:4} | {student_section:3} |' + '\n'
    msg += '------------------------------------------------------------------------------' + '\n'
    msg_label.configure(text = msg)

def search_by_rollno():
    rollno = entry_rollno.get()
    query1 = f'SELECT * FROM marksheet WHERE rollno = {rollno}'
    cursor.execute(query1)
    result = cursor.fetchall()
    msg_label.configure(text = result)
    entry_rollno.delete(0, tk.END)

def search_by_name():
    name = entry_name.get()
    query1 = f"SELECT * FROM marksheet WHERE name LIKE '{name}'"
    print(query1)
    cursor.execute(query1)
    result = cursor.fetchall()
    msg_label.configure(text = result)
    entry_name.delete(0, tk.END)


def delete_by_rollno():
    rollno = entry_rollno.get()
    query2 = f'DELETE FROM marksheet WHERE rollno = {rollno};'
    print(query2)
    entry_rollno.delete(0, tk.END)
    connection.commit()


def delete_by_name():
    name = entry_name.get()
    query = "DELETE FROM marksheet WHERE name LIKE %s"
    values = (name,)
    cursor.execute(query, values)
    entry_name.delete(0, tk.END)
    connection.commit()
  
root_window = tk.Tk()
root_window.title('Student management system')
heading = tk.Label(root_window, text = 'Student management system')
label_rollno = tk.Label(root_window, text = 'Enter student roll number')
entry_rollno = tk.Entry(root_window)
search_rollno = tk.Button(root_window, text = 'Search', command = search_by_rollno)
delete_rollno = tk.Button(root_window, text = 'Delete', command = delete_by_rollno)
label_name = tk.Label(root_window, text = 'Enter student name')
entry_name = tk.Entry(root_window)
search_name = tk.Button(root_window, text = 'Search', command = search_by_name)
delete_name = tk.Button(root_window, text = 'Delete', command = delete_by_name)
label_marks = tk.Label(root_window, text = 'Enter student marks')
entry_marks = tk.Entry(root_window)
label_grade = tk.Label(root_window, text = 'Enter student grade')
entry_grade =  tk.Entry(root_window)
label_section = tk.Label(root_window, text = 'Enter student section')
entry_section = tk.Entry(root_window)
button_add = tk.Button(root_window, text = 'Add student', command = entering)
button_show = tk.Button(root_window, text = 'Show all', command = showing)
msg_label = tk.Label(root_window, text = '', font = ('Courier New', 8, 'bold'))

heading.grid(row = 0, columnspan = 2)
label_rollno.grid(row = 1, column = 0)
entry_rollno.grid(row = 1, column = 1)
search_rollno.grid(row = 1, column = 2)
delete_rollno.grid(row = 1, column  = 3)
label_name.grid(row = 2, column = 0)
entry_name.grid(row = 2, column = 1)
search_name.grid(row = 2, column = 2)
delete_name.grid(row = 2, column = 3)
label_marks.grid(row = 3, column = 0)
entry_marks.grid(row = 3, column = 1)
label_grade.grid(row = 4, column = 0)
entry_grade.grid(row = 4, column = 1)
label_section.grid(row = 5, column = 0)
entry_section.grid(row = 5, column = 1)
button_add.grid(row = 6, column = 0)
button_show.grid(row = 6, column = 1)
msg_label.grid(row = 7, columnspan = 2)
root_window.mainloop()


    
