import pymysql as bot


rollno = int(input('Enter roll no:'))
name = input('Enter name:')
marks = float(input('Enter marks:'))
grade = input('Enter grade:')
section = input('Enter section:')
try:
    connection = bot.connect(
        host = "localhost",
        user = "root",
        password = "Tiger@123",
        database = "school"
        )

    print('Connected')
    cursor = connection.cursor()
    query = 'INSERT INTO marksheet(rollno, name, marks, grade, section) VALUES(%s, %s, %s, %s, %s)'
    values = (rollno, name, marks, grade, section)
    cursor.execute(query, values)
    connection.commit()

    
except:
    print('Something went wrong')

finally:
    if 'connection' in locals and connection.is_connected():
        connection.close()