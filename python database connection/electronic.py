import mysql.connector 


# connect to mysql
mydb = mysql.connector.connect(
host="localhost",                   #or your server host
user="root",                        #your mysql username
password="130096",                  #your mysql password
database="electronic"  #optional: the DB to use

)

print("connection success")


# create a cursor object 
mycursor=mydb.cursor()


mycursor.execute("""
create table if not exists orders (
    orderID INT,
     CustomerName VARCHAR (255),
     Product VARCHAR (255),
     Quantity INT,
     Price DECIMAL(10,2)                                                
    )             
 """)

print("table created successfully")


sql="insert into orders(CustomerName,Product,Quantity,Price) values(%s, %s, %s, %s)"
values=[
    ("Alice","Laptop",2,55000.00),
    ("Bob","Chair",5,3000.00),
    ("Charlie","Table",1,7000.00),
    ("David","Laptop",1,55000.00),
    ("Eve","Mouse",10,500.00)
]

mycursor.executemany(sql,values)
mydb.commit()

print(mycursor.rowcount,"record inserted.")


# Average price 

mycursor.execute("select avg(price) from orders")
avg_price = mycursor.fetchone()[0]
print("average price:", avg_price)


# Sum of Quantity
mycursor.execute("select sum(quantity) from orders")
sum_quantity = mycursor.fetchone ()[0]
print("total quantity sold:",sum_quantity)


# Min price 
mycursor.execute("select min(price) from orders")
min_price = mycursor.fetchone()[0]
print("minimum price:",min_price)


# Count orders 
mycursor.execute("select count(*) from orders")
count_orders = mycursor.fetchone()[0]
print("total orders:",count_orders)


# Max price 
mycursor.execute("select max(price) from orders")
max_price = mycursor.fetchone()[0]
print("max price:",max_price)



# UPDATE: INcrise price of mouse to 600
sql = "update orders set price = %s where product = %s"
val = (600.00,"mouse")

mycursor.execute(sql,val)
mydb.commit()

print(mycursor.rowcount,"record(s) updated.")



# Delete orders where product = 'chair'
sql = "delete from orders where product =%s"
val = ("chair",)

mycursor.execute(sql,val)
mydb.commit()

print(mycursor.rowcount,"record(s) deleted.")

