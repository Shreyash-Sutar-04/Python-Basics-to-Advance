Menucard = ["cocacola = $2","thumbs up = $3.5","mazza = $4","pepsi = $6","limca=$1"]
for menu in Menucard:
    print(menu, end = "\n")


order = []
total_amount = []
total = 0

while True:
    purchase = input("Enter the baverage you  would like to buy :" )
    if purchase == "quit":
        break
    else:
        price = float(input(f"Enter the price of {purchase} as per menucard : $"))
        order.append(purchase)
        total_amount.append(price)

print("---------- YOUR PURCHASE ----------")
for item in order:
    print(item, end="\n")

for sumation in total_amount:
    total = total+sumation
print(f"Your total bill is ${total}.")