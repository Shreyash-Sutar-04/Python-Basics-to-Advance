# Nested Loop = A loop within the another loop 
# While This Indentation is an important step 
'''
outer loop:
    inner loop:
'''
# You can have a while loop inside while loop for loop inside for loop while inside for loop and vice versa

# for x in range(3):
#     for y in range(1,10):
#         print(y, end="")
#     print()

rows = int(input("Enter the numbers of rows : "))
columns = int(input("Enter the numbers of columns : "))
symbol = input("Enter the symbol :")
for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()