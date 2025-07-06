x = ("apple","banaba","cherry")
y = list (x)
y[1] = "mango"
x = tuple(y)

print(x)

y.append("orange")
x = tuple(y)
print(y)