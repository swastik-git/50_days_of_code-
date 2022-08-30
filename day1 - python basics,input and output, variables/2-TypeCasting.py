import types


# Types conversion of 2 types
# 1 - implicit - the Python interpreter automatically converts one data type to another without any user involvement
# Ex- 
x = 10

print("x is of type:",type(x))

y = 10.6
print("y is of type:",type(y))

z = x + y

print(z)
print("z is of type:",type(z))


# 2 - explicit - the data type is manually changed by the user as per their requirement. With explicit type conversion, there is a risk of data loss since we are forcing an expression to be changed in some specific data type
s = '101011'
print(type(s))
e = float(s)
print ("After converting to float : ", end="")
print (e)
print(type(e))

