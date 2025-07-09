import mysql.connector

# connect to mysql 
mydb = mysql.connector.connect(
 host = "localhost",
 user = "root",
 password = "130096",
 database = "python_mysql_connection3"   

)

print("connection success")


# create a cursor object 
mycursor = mydb.cursor()


mycursor.execute("""
create table if not exists emp (
                 id int ,
                 name VARCHAr(255),
                 age int
                               
                 )

""")

print("table created successfully")




# insert data 

sql = "insert into Doctor(id,name,age) values (%s,%s,%s)"
val = (302,"sutar",32)
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"recoed inserted")


