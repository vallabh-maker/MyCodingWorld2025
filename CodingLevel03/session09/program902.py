
def execution():
    mydb = bot.connect(
        host = "localhost",
        user = "root",
        password = "Tiger@123",
        database = "vallabh_company"
    )

    if mydb == None:
        print('Not connected')
    else:
        print('Connected')

        cursor = mydb.cursor()
        query = 'SELECT * FROM Department'
        cursor.execute(query)

        list_of_rows = cursor.fetchall()

        deptno = 'No.'
        deptname = 'Department name'
        deptloc = 'Location'

        msg = ''      
        msg += '--------------------------------------------' + '\n'
        msg += f'| {deptno:4} | {deptname:15} | {deptloc:15} |' + '\n'
        msg += '--------------------------------------------' + '\n'
        for record in list_of_rows:
            deptno = record[0]
            deptname = record[1]
            deptloc = record[2]
            msg += f'| {deptno:4} | {deptname:15} | {deptloc:15} |' + '\n'
        msg += '--------------------------------------------' + '\n'
        msg_label.configure(text = msg)

#Main
import pymysql as bot
import tkinter as tk

root_window = tk.Tk()
msg_label = tk.Label(root_window, text = '')

button = tk.Button(root_window, text = 'display table', command = execution)

button.grid(row = 0, column = 0)
msg_label.grid(row = 1, column = 1)
root_window.mainloop()

