from datetime import date
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="130096",
    database="employeeconnection"

)
print("connection succesfull")



mycursor = mydb.cursor()

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        empID INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        department VARCHAR(50),
        salary DECIMAL(10,2),
        joinDate DATE
    )
""")

print("Employee table created successfully.")

sql="insert into employee(name,department,salary,joindate) values (%s, %s, %s, %s)"
values = [
    ("alice", "hr", 50000.00, date(2020, 1, 15)),
    ("bob", "it", 75000.00, date(2019,5,10)),
    ("charlie", "finance", 62000.00, date(2021,7,22)),
    ("david", "it", 80000.00, date(2018,3,18)),
    ("eva", "hr", 48000.00, date(2022,2,28))
]

mycursor.executemany(sql, values)

mydb.commit()

print(mycursor.rowcount,"records inserted.")


mycursor = mydb.cursor()

sql= "update employee set salary = salary + 5000 where department = 'hr'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount,"record(s) update.")



mycursor = mydb.cursor()

mycursor.execute("select avg(salary) from employee")
print("average salary:", mycursor.fetchone()[0])


mycursor.execute("select sum(salary) from employee")
print("total salary:", mycursor.fetchone()[0])


mycursor.execute("select min(salary) from employee")
print("minimum salary:", mycursor.fetchone()[0])


mycursor.execute("select max(salary) from employee")
print("maximum salary:", mycursor.fetchone()[0])


mycursor.execute("select count(*) from employee")
print("total employee:", mycursor.fetchone()[0])

