"""
Validate user input exercise
1. Username is no more then 12 character
2. User name must not contain spaces
3. username must not contain digits 
"""
username = input("Enter the name :")

if len(username)>12:
    print("Length of username is violated!")
elif not username.find(" ") == -1:
    print("Username should not contain spaces!")
elif not username.isalpha():
    print("Username must not contain spaces!!!")
else:
    print(f"Yeah! you are good to go {username}")