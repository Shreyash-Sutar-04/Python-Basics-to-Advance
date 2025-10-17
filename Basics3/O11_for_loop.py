# Demonstration of for loop iteration over string
credit_card = "1234-5678-9012-3456"
for c in credit_card:
    print(c)

# Lets print number except a number 
#  Means if you want to print the numbers and dont want any particular number that time we use continue keyword for it
for i in range(1,21):
    if i == 13:
        continue
    else:
        print(i)

# Break keyword demonstration
for i in range(1,21):
    if i == 13:
        break
    else:
        print(i)
