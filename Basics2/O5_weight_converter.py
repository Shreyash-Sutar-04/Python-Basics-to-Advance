# Python Weight converter

# weight = float(input("Enter your Weight : "))
# unit = input("Is it kilogram/Pounds? (k/l) : ")

# if unit == "k":
#     print(f"Your Weight is {weight*2.20462} Pounds.")
# elif unit == "l":
#     print(f"Your Weight is {weight/2.20462} Kilograms.")
# else:
#     print(f"Provided wrong unit {unit}")


# weight = float(input("Enter Your Weight:"))
# unit = input("Is it Kg or Pounds? K/P :")

# if unit == "K" :
#     print(f"Your Weight in pounds is {round(weight*2.20462 ,2)}")
# elif unit == "P":
#     print(f"Your Weight in KiloGrams is {round(weight/2.20462 ,2)}")
# else :
#     print(f"Provided {unit} is Invalid")


weight = float(input("Enter Your Weight:"))
unit = input("Is it Kg or Pounds? K/P :")

if unit == "K" :
    weight = round(weight*2.20462 ,2)
    unit = "LBS"
    print(f"Your Weight is {weight} {unit}")
elif unit == "P":
    weight = rount(weight/2.20462,2)
    unit = "Kilograms"
    print(f"Your Weight is {weight} {unit}")
else:
    print(f"Provided {unit} is Invalid")

 