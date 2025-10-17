#Enter your favourite food untill you want to quit

food = input("Enter the names of food you like:")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter the names of food you like:")

print("ohh Thats it!")