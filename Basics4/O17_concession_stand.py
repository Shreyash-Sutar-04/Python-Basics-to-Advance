menu = {"Lemon Soda": 20,
        "Jira Soda":15,
        "Blueberry Soda":50,
        "Black Current Soda":100,
        "Lemonade":10,
        "Cocacola":30,
        "Sprite":15}

cart = []
total = 0

print("----------SODA CENTER------------")
for key,value in menu.items():
    print(f"{key:20} :{value:.2f}₹")
print("---------------------------------")

while True:
    type = input("Enter Soda would you like to have: ")
    if type == "q":
        break
    elif menu.get(type) is not None:
       cart.append(type)

print("------Your Choices------")
for items in cart:
    total = total+menu.get(items)
    print(f" {items:10}")
print()

print(f"Sir your total bill is : {total}₹")



