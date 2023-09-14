import mysql.connector 

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='new123pass$'
)

cursorObj = dataBase.cursor()

cursorObj.execute("CREATE DATABASE elderco")

print("All Done !")