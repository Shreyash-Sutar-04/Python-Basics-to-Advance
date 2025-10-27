#Concession stand program in python
menu = {"pizza" : 3.00,
        "nachos":4.50,
        "popcorn":6.00,
        "fries":2.50,
        "chips":1.00,
        "pretzel":3.50,
        "soda":3.00,
        "lemonade":4.25}
cart = []
total = 0

print("-------MENUCARD-------")
for key,value in menu.items():
        print(f"{key:8} : ${value: .2f}")
print("-----------------------")

while True:
        food = input("What Would you like to have? (press q for quit) : ")
        if food == "q":
                break
        elif menu.get(food) is not None:
                cart.append(food) #This is if user will select the item outside the menu

for items in cart:
        total += menu.get(items)
        print(f"{items:.10}")

print()
print(f"Your total bill is ${total}." )