import mysql.connector 

# connect to mysql
mydb = mysql.connector.connect(
host="localhost",                   #or your server host
user="root",                        #your mysql username
password="130096",                  #your mysql password
database="python_mysql_connection"  #optional: the DB to use

)

print("connection success")


# create a cursor object 
mycursor=mydb.cursor()


# mycursor.execute("""
# create table if not exists students (
#     id int,
#     name varchar(255),
#     age int
#     )             
#  """)

# print("table created successfully")

#insert data 
sql="insert into students (name,age) values (%s,%s)"
val= ("john",21)
mycursor.execute(sql,val)
mydb.commit ()
print(mycursor.rowcount,"recoed inserted.")