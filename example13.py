#  Merge two dictionaries into one.


x = {
    "cars" : "swift",
    "Bike" : "KTM",
    "Fruits" : "Apple"
}
    

y = {
    "name": "Sushant",
    "age": 25,
    "city": "Pune"
}



z = {**x,**y}
print(z)