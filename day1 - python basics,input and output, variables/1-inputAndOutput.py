# get input using input() function
name = input("Enter your name: ")

# taking multiple inputs 
# by default input() returns string we can convert it to int using int() or float using float() 
x,y,z = input("enter 3 numbers: ").split()

#split function by default split using ' ' blank space

#output using print() function
print("Hello")
 
# printfunction parameters print(values,sep,end,flush)
print("Hello!", name)

# print which not ends with next line but ends with space
print("Hello",end=" ")
print(f"My name is {name}") #output formating using f string

# output formating using .format()
print("First number is {} , second number is {} and third number is {}".format(x,y,z))


#using sep keyword in print()

a=12
b=12
c=2022
print(a,b,c,sep="-")


cstr = "I love you"
   
# Printing the center aligned 
# string with fillchr
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '#'))
 
# Printing the left aligned 
# string with "-" padding 
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))
 
# Printing the right aligned string
# with "-" padding 
print ("The right aligned string is : ")
print (cstr.rjust(40, '-'))