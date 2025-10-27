'''
A 2D keypad is a keypad you see in your phone how its made is as following
'''

# as we think about it we will got to know that we have 3 datatypes i.e tuples,lists,sets
# The sets are unordered so we cant use that and if you think of list and tuple the tuple is faster then list so we will go for tuple

numpad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))
for row in numpad:
    for num in row:
        print(num, end= " ")
    print() #This is to add newline after each row 
 