import pymysql as bot



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