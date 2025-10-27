# Dictionary = A collection of {key:value} pairs
#               ordered and changable. No duplicates

capitals = {"USA" : "Washington DC",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"} 
#This is how the dictionaries are made

# TO know about the functions or methods related to dictionary 
# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA")) #To get the value of any key
print(capitals.get("Moscow")) # If you provide value in terms of getting key in return it will return just nons
print(capitals.get("Japan")) # Well even if the key doesnot exist in your dictionary then it simply returns none

#key element with if else looping
name = input("Enter the country name to find out its capital: ")
if capitals.get(name):
    print("Capital does not exist")
else:
    print("That capital does not exist!!!")

#Update the dictionery
# In the sense 2 ways
print(capitals)
capitals.update({"Germany":"Berlin"}) #To add new value
capitals.update({"USA":"Detroit"}) # To change the prerequsite key
print(capitals) 

#Removing the key value pair from the dictionary
# You cannot remove the "latest" key value by this method 
capitals.pop("USA")
print(capitals)
#Well If you want to remove the latest key value pair then you have to just use following method
capitals.popitem()
print(capitals)

print(len(capitals))

