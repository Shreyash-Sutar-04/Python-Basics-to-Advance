name = input("Enter Yout full name: ")
print(len(name))

result = name.find(" ")
print(result)
"""
This above method will 
find the first occurance of whatever you will provide like,
or space or any character or full stop,etc.
"""
#if you want the last recurrance then add r in find like below
Last_Occurance = name.rfind(" ")
print(Last_Occurance)
# in these cases it starts counting from 0

name = name.capitalize()
print(name)

name = name.upper()
print(name)

numerical = name.isdigit()
print(numerical)

# Example 1: All alphabetic characters
str1 = "HelloWorld"
print(str1.isalpha())  # Output: True

# Example 2: Contains numbers
str2 = "Python123"
print(str2.isalpha())  # Output: False

# Example 3: Contains spaces
str3 = "Hello World"
print(str3.isalpha())  # Output: False

phone_number = "+91 8485898732"
result = phone_number.count("+")
print(result)

phone_number = phone_number.replace("+","-")
print(phone_number)