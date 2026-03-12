#import extensions
import pymysql as bot
import tkinter as tk
#defining function to add an employee
def add_employee():
    empno = entry_empno.get()
    ename = entry_empname.get()
    job = entry_job.get()
    mgr = entry_mgr.get()
    hiredate = entry_hiredate.get()
    sal = entry_sal.get()
    comm = entry_comm.get()
    deptno = deptno_var.get()
    query = 'INSERT INTO employee(empno, ename, job, mgr, hiredate, sal, comm, deptno) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
    values = (empno, ename, job, mgr, hiredate, sal, comm, deptno)
    cursor.execute(query, values)
    connection.commit()
    entry_empno.delete(0, tk.END)
    entry_empname.delete(0, tk.END)
    entry_job.delete(0, tk.END)
    entry_mgr.delete(0, tk.END)
    entry_hiredate.delete(0, tk.END)
    entry_sal.delete(0, tk.END)
    entry_comm.delete(0, tk.END)
def display_all():
    query = 'SELECT * FROM employee'
    cursor.execute(query)
    list_of_rows = cursor.fetchall()
    empno = 'Employee Number'
    ename = 'Employee Name'
    job = 'Job'
    mgr = 'Manager'
    hiredate = 'Hire Date'
    sal = 'Salary'
    comm = 'Commision'
    deptno = 'Department Number'
    msg = ''
    msg += '----------------------------------------------------------------------------------------------------------------------------' + '\n'
    msg += f'| {empno:15} | {ename:20} | {job:12} | {mgr:8} | {hiredate:10} | {sal:8} | {comm:8} | {deptno:17} |' + '\n'
    for record in list_of_rows:
        empno = record[0]
        ename = record[1]
        job = record[2]
        mgr = record[3]
        if mgr == None:
            mgr = 'None'
        hiredate = record[4]
        sal = record[5]
        comm = record[6]
        if comm == None:
            comm = 'None'
        deptno = record[7]
        msg += f'| {empno:15} | {ename:20} | {job:12} | {mgr:8} | {hiredate:10} | {sal:8} | {comm:8} | {deptno:17} |' + '\n'
    msg += '----------------------------------------------------------------------------------------------------------------------------' + '\n'
    msg_label.configure(text = msg)

def update_employee():
    empno = entry_empno.get()
    ename = entry_empname.get()
    job = entry_job.get()
    mgr = entry_mgr.get()
    hiredate = entry_hiredate.get()
    sal = entry_sal.get()
    comm = entry_comm.get()
    deptno = deptno_var.get()
    query = 'UPDATE employee SET ename = %s, job = %s, mgr = %s, hiredate = %s, sal = %s, comm = %s, deptno = %s WHERE empno = %s'
    values = (ename, job, mgr, hiredate, sal, comm, deptno, empno)
    cursor.execute(query, values)
    connection.commit()
    entry_empno.delete(0, tk.END)
    entry_empname.delete(0, tk.END)
    entry_job.delete(0, tk.END)
    entry_mgr.delete(0, tk.END)
    entry_hiredate.delete(0, tk.END)
    entry_sal.delete(0, tk.END)
    entry_comm.delete(0, tk.END)
def search_by_empno():
    empno = entry_empno.get()
    query = f'SELECT * FROM employee WHERE empno = {empno}'
    cursor.execute(query)
    result = cursor.fetchall()
    msg_label.configure(text = result)
    connection.commit()
    entry_empno.delete(0, tk.END)

def delete_by_empno():
    empno = entry_empno.get()
    query = f'DELETE FROM employee WHERE empno = {empno}'
    cursor.execute(query)
    connection.commit()
    entry_empno.delete(0, tk.END)

def search_by_ename():
    ename = entry_empname.get()
    query = f'SELECT * FROM employee WHERE ename = {ename}'
    cursor.execute(query)
    result = cursor.fetchall()
    msg_label.configure(text = result)
    connection.commit()
    entry_empname.delete(0, tk.END)

def delete_by_ename():
    ename = entry_empno.get()
    query = f"DELETE FROM employee WHERE ename = '{ename}'"
    cursor.execute(query)
    connection.commit()
    entry_empno.delete(0, tk.END)
#connect to the database
connection = bot.connect(
    host = "localhost",
    user = "root",
    password = "Tiger@123",
    database = "vallabh_company"
    )
cursor = connection.cursor()
#creating the GUI and all the elements of the GUI
root_window = tk.Tk()
root_window.title('Employee & Department Management System')
#Labels, entries and buttons of the 'employee' table
heading = tk.Label(root_window, text = 'Employee & Department Management System', font = ('Courier New', 12, 'bold'))
label_empno = tk.Label(root_window, text = 'Enter Employee Number')
entry_empno = tk.Entry(root_window)
button_empno = tk.Button(root_window, text = 'Search', command = search_by_empno)
delete_empno = tk.Button(root_window, text = 'Delete', command = delete_by_empno)
label_empname = tk.Label(root_window, text = 'Enter Employee Name')
entry_empname= tk.Entry(root_window)
button_empname = tk.Button(root_window, text = 'Search', command = search_by_ename)
delete_empname = tk.Button(root_window, text = 'Delete', command = delete_by_ename)
label_job = tk.Label(root_window, text = 'Enter Job')
entry_job = tk.Entry(root_window)
label_mgr = tk.Label(root_window, text = 'Enter Manager')
entry_mgr = tk.Entry(root_window)
label_hiredate = tk.Label(root_window, text = 'Enter Hire Date')
entry_hiredate = tk.Entry(root_window)
label_sal = tk.Label(root_window, text = 'Enter Salary')
entry_sal = tk.Entry(root_window)
label_comm = tk.Label(root_window, text = 'Enter Commission')
entry_comm = tk.Entry(root_window)
#Creating the dropdown menu for department number
label_deptno = tk.Label(root_window, text = 'Enter Department Number')
deptno_var = tk.StringVar(value = 'Department Number')
options = [10, 20, 30, 40, 50, 60]
entry_deptno = tk.OptionMenu(root_window, deptno_var, *options)
#Creating the buttons to display and update employee details
button_add = tk.Button(root_window, text = 'Add Employee', command = add_employee)
button_display = tk.Button(root_window, text = 'Display All Employees', command = display_all)
button_update = tk.Button(root_window, text = 'Update Employee Details', command = update_employee)
msg_label = tk.Label(root_window, text = '', font = ('Courier New', 10))


#Displaying all the labels, buttons and entries
heading.grid(row = 0, columnspan = 4)
label_empno.grid(row = 1, column = 0)
entry_empno.grid(row = 1, column = 1)
button_empno.grid(row = 1, column = 2)
delete_empno.grid(row = 1, column = 3)
label_empname.grid(row = 2, column = 0)
entry_empname.grid(row = 2, column = 1)
button_empname.grid(row = 2, column = 2)
delete_empname.grid(row = 2, column = 3)
label_job.grid(row = 3, column = 0)
entry_job.grid(row = 3, column = 1)
label_mgr.grid(row = 4, column = 0)
entry_mgr.grid(row = 4, column = 1)
label_hiredate.grid(row = 5, column = 0)
entry_hiredate.grid(row = 5, column = 1)
label_sal.grid(row = 6, column = 0)
entry_sal.grid(row = 6, column = 1)
label_comm.grid(row = 7, column = 0)
entry_comm.grid(row = 7, column = 1)
label_deptno.grid(row = 8, column = 0)
entry_deptno.grid(row = 8, column = 1)
button_add.grid(row = 9, column = 0)
button_display.grid(row = 9, column = 1)
button_update.grid(row = 9, column = 2, columnspan = 2)
msg_label.grid(row = 10, columnspan = 4)
root_window.mainloop()


#make outputs case insensitive and ensure there is an error statement if employee does not exist