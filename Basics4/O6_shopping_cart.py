menu = ["apple juice","banana shake","mango shake","pineapple juice","strawberry juice"]
print(menu,end="\n") #This will not work because here we are printing the entire list as is 
# To print elements one by one from the list you have to 
for item in menu:
    print(item,end="\n")

order = []
price = []
total_amount = 0

while True:
    item = input("Enter the name of shake or juice you want (type done if the order is done): ")
    if item == "done":
        break
    else:
        value = float(input("Enter the price of each juice : $"))
        order.append(item)
        price.append(value)

print("----------- YOUR CART ------------")

for k in order:
    print(k,end="\n")

for p in price:
    total_amount = total_amount+p

print(f"Your total bill is {total_amount}")