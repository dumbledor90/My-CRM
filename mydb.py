import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1111',
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database 
cursorObject.execute("CREATE DATABASE lumidb")

print('All done!')
