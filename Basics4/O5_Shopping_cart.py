# Shopping cart program

Menu = ["pizza = $12","burger = $10","pasta = $4.8","ramen = $15.5","nooodles = $4.5","soup = $12.0","poriedge = $2.3","salad = $1.4"]
print(Menu) 
order = []
prices = []
total = 0

while True:
    food = input("What Would you like to buy sir? : ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}: $"))
        order.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in order:
    print(food)

for price in prices:
    total = total+price
print(f"Your total bill is {total}")

