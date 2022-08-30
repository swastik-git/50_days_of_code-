# variable is a name of any memory location

a = 10  #int types variable
b = 10.50 #float types
c = True;d = False      #boolean types etc

# Diffrent dataTypes in python

# Text Type: 	str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	NoneType



# Checking dataTypes
# You can get the data type of any object by using the type() function:
a = 10
print(type(a))

# setting the datatypes of variable
#  1 the data type is set when you assign a value to a variable
#  2 If we want to specify the data type, we can use the constructor functions:     ex- 

a = int()
b = float()
c = str()
x = str("Hello World")

xl = list(("apple", "banana", "cherry")) 	 	
xt= tuple(("apple", "banana", "cherry")) 	
xr = range(6)
# etc




# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# Maximum possible value of and int in python 
# is not restricted by the number of bits and can expand to the limit of the available memory 

a = 10000000000000000000241201545215
print("a =",a)
print(type(a))

b = 50
print("b = ",b)
print(type(b))




# Local and global variables

# Local
def f():

	# local variable
	s = "I love Geeksforgeeks"
	print(s)


# Driver code
f()


# Global

# 1
# This function uses global variable s
def f():
	print("Inside Function", s)

# Global scope
s = "I love Geeksforgeeks"
f()
print("Outside Function", s)

# 2
def f():
	s = "Me too."
	print(s)


# Global scope
s = "I love Geeksforgeeks"
f()
print(s)



# Global Keyword:
# We only need to use the global keyword in a function if we want to do assignments or change the global variable
# To tell Python, that we want to use the global variable, we have to use the keyword “global”, as can be seen in the following example: . 

# This function modifies the global variable 's'
def f():
	global s
	s += ' GFG'
	print(s)
	s = "Look for Geeksforgeeks Python Section"
	print(s)

# Global Scope
s = "Python is great!"
f()
print(s)




