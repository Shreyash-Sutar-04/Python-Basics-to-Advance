"""
2D Lists == A 2Dimensional lists are the list made by multiple lists

"""
fruits = ["mango","banana","apple","guava","grapes"]
cars =   ["golf GTI","Camaro","Camry","Mini cooper","Alto 800"]
Bikes =  ["Continental GT","Jawa Scrambler","Royal Enfield Classic 350","Honda Xpulse","Klx 230"]

collections = [fruits,cars,Bikes] # <--- This is a 2D list as you can see the elements for 2D list is singular list names
print(collections[0])
print(collections[1])
print(collections[2])
#This is how we print the entire list because 2D list treat the no of lists as a metrix
#Now if you want to print a single element from the list
print(collections[0][0])
print(collections[0][1])
print(collections[1][0])
print(collections[2][4])
print(len(collections)) #This will return a 3 because the list itself is element for 2D collection



