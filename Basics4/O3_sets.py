#Everything happens randomly 

fruits = {"sunday","monday","tuesday","wednesday","sunday"}
print(fruits)

# Duplications doesnt happen here
# The duplicate element will be printed once

# The sets are unordered because if you print the set everytime you will notice that the order of elements is changed!
print(len(fruits))
print("sunday" in fruits)

# print(fruits[0]) #Error set object is not subscriptable

fruits.add("kivi")
print(fruits)

# pop method will remove the very first element
fruits.pop()
print(fruits)

