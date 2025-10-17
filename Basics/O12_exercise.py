import math

side1 = int(input("Enter the side A :"))
side2 = int(input("Enter the side B :"))

hypotenous = math.sqrt(pow(side1,2) + pow(side2,2))
print(f"The hypotenous of the right angled triangle is {hypotenous} ")
