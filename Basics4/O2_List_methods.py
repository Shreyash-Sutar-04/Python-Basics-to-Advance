fruits = ["Kivi","Kivi","Guava","Grapes","Banana","Apple","Mango"]

#Sorting
print("Before alphabetical order")
print(fruits)
fruits.sort()
print("After alphabetical order")
print(fruits)

#Reverse order 
cars = ["Polo Golf GTI","Honda Civic","Toyota Hilux","Chervolte Camaro","Toyota Camry"]
cars.reverse()
print(cars)

#Reverse alphabetical order
# To get it first sort and then reverse
cars.sort()
print(cars)
cars.reverse()
print(cars)

#clear the list
# cars.clear()
# print(cars)
# print(len(cars))

#Print the index of element
print(cars.index("Toyota Camry"))
print(cars.index("Toyota Hilux"))

#Print the element how many times appeared
print(fruits.count("Kivi"))