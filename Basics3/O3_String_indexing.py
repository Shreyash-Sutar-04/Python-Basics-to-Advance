"""
[] ==> This square braces in terms of python known as Indexing Operators
String Indexing means acessing elements of the sequence from string using []
[start : end : step]
"""
credit_card =  "1234-5678-9012-3456"
print(credit_card[10]) #Can target one digit starting the string always with 0
print(credit_card[0:4])#In this case you have given the start and end point so doesnot start counting from 0
print(credit_card[-5]) #Start from end
print(credit_card[::2])#this skips the every second character start from first character
print(credit_card[1:6]) 
print(credit_card[1:6:2]) 

#Practical Example
last_digits = credit_card[-4:]
print(f"Youre credit card number is XXXX-XXXX-XXXX-{last_digits}")