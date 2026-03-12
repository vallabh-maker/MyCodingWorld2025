import pymysql as bot
import tkinter as tk
def extract_for_rollno():
    mydb = bot.connect(
        host = "localhost",
        user = "root",
        password = "Tiger@123",
        database = "vallabh_company"
    )
    cursor = mydb.cursor()
    query = f'SELECT * FROM student WHERE rollno = '
    cursor.execute(query)
    list_of_rows = cursor.fetchall()
    name = 'name'
    marks = 'marks'
    grade = 'grade'
    section = 'section'