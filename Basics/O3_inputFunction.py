'''
input() :- A function that prompts the user to enter data and 
           returns the entered data as a string
'''
# input() #here we are just taking the user input

# input("Enter your name:") # Here we Add the prompt within quotes so that user could understand what to type

name = input("What's Youre Name:- ")
print(f"Hey There {name}!")
print(type(name)) # here even if we take user input 20 something it will still show the type as string


age =  input("how old are you? :- ")
age = int(age) # Since it return the string we have to xplicitly convert it into integer
age = age+1
print(f"You will be {age} next year!")
#This is kinda mess there is an alternative method

price = int(input("Nice Watch! How much does it costs?")) #we can do this way too!
print(f"{price} Are you kidding me!!")
print(type(price))