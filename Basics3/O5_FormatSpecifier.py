'''
When formatting strings or numbers in Python (like using format() or f"{...:...}"),
flags are special characters that control how the output looks — alignment, sign, padding, etc.
format specifier ==> format() or f"{variable_defined}"
The conctruction of format specifier is {value:flags} it means format the value in format specifier based on 
flags are inserted!
.(number)f = round to that many decimal places (fixed point)
:(number) = allocate that many spaces
:03 = allocate and zero pad that many spaces
:< = left justify
:> = right justify
:^ = center align
:+ = use a plus sign to indicate positive value
:= = place sign to leftmost position
:  = insert a space before positive numbers
:, = comma separator
'''

price1 = 3.14159
price2 = -987.65
price3 = 12.34

# print(f"price1 is ${price1:.2f}")
# print(f"price2 is ${price2:.2f}")
# print(f"price3 is ${price3:.2f}")
#This will print these values in float number upto 2 decimal numbers
# if you go for suppose 3f the python automatically concatinate additional 0s like in case of 3rd price

# print(f"price1 is {price1:10}")
# print(f"price2 is {price2:10}")
# print(f"price3 is {price3:10}")
# Specifies how much space the value should allocate!

# print(f"price1 is {price1:010}")
# print(f"price2 is {price2:010}")
# print(f"price3 is {price3:010}")
#In this case each number will be 0 padded unless and untill,it fullfills the entire 10 digit space

# print(f"price1 is {price1:<10}")
# print(f"price2 is {price2:<10}")
# print(f"price3 is {price3:<10}") #----Left Justifiation
# print(f"price1 is {price1:>10}")
# print(f"price2 is {price2:>10}")
# print(f"price3 is {price3:>10}") #---Right Justification
# print(f"price1 is {price1:^10}")
# print(f"price2 is {price2:^10}")
# print(f"price3 is {price3:^10}") #---Center Allignment

price1 = 30000.14159
price2 = -98700.65
price3 = 12000.34
#Now these value when we want to print in Comma separated at hundreds,thousands place
print(f"price1 is ${price1:,.2f}")
print(f"price2 is ${price2:,.2f}")
print(f"price3 is ${price3:,.2f}")
#Also next to it we can add the value should be upto 2 decimal 
#Add +sign before comma and see what happens It will simply add + to positive decimal values!




