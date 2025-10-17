# Typecasting is the process of converting a variable from one data type into another datatype
# str(),int(),float(),bool()
# We use "type" named function to determne the type of variable
# it will be usefull to modify user inputs

name = "Shreyash"
age = 22
gpa = 7.0
price = 200
is_fresher = False

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_fresher))

#Conversion
gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

is_fresher = int(is_fresher)
print(is_fresher)
'''
Based on the value of boolean function Whether it is True or False the int typecasting will return 1 or 0 respectively.
'''

age = str(age)
print(type(age))
print(age)

# String Concatination
price = str(price)
print(price)
price+="1" #Since we are adding string so it should be in double inverted comma
print(price)

# Empty string boolean type casting scenario
name = ""
name = bool(name)
print(name) #if the string is empty it will return false
