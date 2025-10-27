
capitals = {"USA" : "Washington DC",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"} 

# To print the all keys we have to use the following method
keys = capitals.keys()
print(keys)
#Technically keys is an object which technically resembles the keys

for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)