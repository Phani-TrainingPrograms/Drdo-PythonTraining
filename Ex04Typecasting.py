# typecasting : Converting the data type of value to another type.

x = 1 # int
y = 2.5 #float
z = "3" # string


x += int(z) # IF U want to add x with z, z being string should be temporarily casted to int.
print(x)
x = y
print(int(y))
# convert int to flaat:
y = float(x);
print(y)

x = 123
y = "234"
print(x + int(y))