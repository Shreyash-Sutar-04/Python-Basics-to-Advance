#Shopping cart program

item = input("What would you like to buy?:")
price = float(input(f"tell me the price for each {item}?" ))
quantity = int(input("Tell me the quantity :"))

total = price*quantity

print(f"for your {quantity} {item}s you have to pay {total} rupees.")