"""
While Loop = Execute some code while some condition remain true
"""

# name = input("Enter your name: ")

# if name == "":
#     print("You did not entered your name!")
# else:
#     print(f"Hello {name}")

# Now in this case if you pass an empty string you will see that the 
# code will stop right after if statement 
# therefore we use the looping concepts

# while name == "":
#     print("Enter the name MORON!")
#     name = input("Enter Your name:")
# print(f"Hello {name}")
#Now in this code if you remove the name input variable from while 
# You might end up with an infinite looping!

age = int(input("Enter your age please:"))
while age < 0 :  # loop continues if a negative number is entered
    print("Please Enter the valid age!")
    age = int(input("Enter Your Age: "))
print(f"Ohh man! Youre {age} years old!")

