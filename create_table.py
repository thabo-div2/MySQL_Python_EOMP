import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="Grimmijow06",
    database="lifechoicesdb2"
)

cursor = db.cursor()

cursor.execute("SHOW TABLES")

tables = cursor.fetchall()

for table in tables:
    print(table)

cursor.execute("DESC admin")

print(cursor.fetchall())

cursor.execute("DESC guest")

print(cursor.fetchall())

cursor.execute("DESC students")

print(cursor.fetchall())
