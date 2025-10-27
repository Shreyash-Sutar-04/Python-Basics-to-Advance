cars = {"camry":1000,
        "Hilux":1200,
        "Mini Cooper":1500,}

# for key,value in cars.items():
#     print(key,value)
#This is how we use the .items() dictionary methid

# The ".get" method give the value its basically related to value of the
name = input("Enter the car name :")
print(cars.get(name))
#This will return none if the key-value does not exist in the list!
# It means its a default value none you can give a diffetrent value as well!


for car in cars:
    print(cars.get(car))
