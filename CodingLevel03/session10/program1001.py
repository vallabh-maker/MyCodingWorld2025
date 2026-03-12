import pymysql as bot

connection = bot.connect(
        host = "localhost",
        user = "root",
        password = "Tiger@123",
        database = "school"
    )

print('Connected')
cursor = connection.cursor()
query = 'INSERT INTO marksheet(rollno, name, marks, grade, section) VALUES(%s, %s, %s, %s, %s)'
values = (116, 'Rajesh', 99.0, 'A+', 'C')
cursor.execute(query, values)
connection.commit()
connection.close()
