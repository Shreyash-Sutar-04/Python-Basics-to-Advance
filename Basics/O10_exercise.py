# take input of radius from user and print circumferance of the circle
import math

Radius = float(input("Enter the radius of the circle :"))
result = 2* math.pi *Radius
print(f"The circumference of the circle is: {result}")
print(round(result)) # you can also provide round upto how many digits
print(round(result,2))
print(math.ceil(result))
print(math.floor(result))