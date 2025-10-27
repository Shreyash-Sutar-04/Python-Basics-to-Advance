"""
collections = A Variable in which we can store multiple values at once
Lists ==> [] ordered and chnagable Duplicate values are allowed!
Set   ==>{} Unordered and immutable can perform add remove. Dulicates are not allowed!
Tuple ==> () Ordered and unchangable. Duplicates are allowed and it's Faster
"""
import time 
fruit = "Apple" #<--- Its an example of string cant store more then one value in it
# That is the limitation over here 

fruits = ["apple","banana","orange","grapes","orange"]
# print(fruits)
# print(fruit)
# List Indexing
# Each value in the collection is also known as element 
# print(fruits[4])
# print(f"The 4th element from the list is {fruits[4]}")

# days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# print(days[::2]) # This will skip every 2nd element we can also mention starting and ending point
# print(days[0:6]) # Output was sunday skipped means the indexing starts from 0

# for x in fruits:
#     time.sleep(1) # This will show the each name at the same place till the last name 1 by 1 each for 1 second
#     print(f"{x}", end="\r")

#Redablity improvement 
# for fruit in fruits:
#     print(fruit)

# print(dir(fruits))
# print(help(fruits))
print(len(fruits))
print("apple" in fruits)
print("grapes" in fruits) # You can use "in" to find if the element is available within the list or not

#Assignment 
fruits[0] = "Kivi"
for fruit in fruits:
    print(fruit)

result = len(fruits)
print(result)

print(fruits) #I thought it will add the element at 0th position named as "kivi" but instead it just 
#Replaces the 0th position element 
#To add an element to the list there is a special method known as "append"

fruits.append("mango") #To add element at last place
print(fruits)
fruits.remove("mango")
print(fruits)
fruits.insert(0,"pineapple") #To add element at a particular place
print(fruits)
fruits.sort() #Will sort the elements in an alphabetical order

# 
