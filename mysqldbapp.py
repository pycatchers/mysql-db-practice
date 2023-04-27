from datetime import date

import mysql.connector

connection = mysql.connector.connect(
    user="paranthaman",
    password="mysql123",
    host="127.0.0.1",
)

cursor = connection.cursor()

# cursor.execute("CREATE DATABASE studentsdb;")

cursor.execute("USE studentsdb;")

# cursor.execute("CREATE TABLE students ("
#                "reg_no int(20) NOT NULL,"
#                "name varchar(50) NOT NULL,"
#                "department varchar(120) NOT NULL,"
#                "email varchar(120) NOT NULL,"
#                "dob date NOT NULL"
#                ");")
# cursor.execute(
#     "INSERT INTO students "
#     "(reg_no, name, department, email, dob) "
#     "VALUES "
#     "(%s, %s, %s, %s, %s)",
#     (1234500, 'harshith', 'ECE', 'harshith@gmail.com', date(2023, 10, 5))
# )

rows = cursor.execute("SELECT * from students;")
myresult = cursor.fetchall()

for row in myresult:
  print(row)


connection.commit()
cursor.close()
connection.close()



