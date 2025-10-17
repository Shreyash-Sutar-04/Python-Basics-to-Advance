# Take user input calculate the area of the circle
import math

Radius = float(input("Provide the Radius if the circle :"))

Result = math.pi * pow(Radius,2)
Result = round(Result,2)
# Result = math.pi*Radius*Radius

print(f"The area of the circle acc to provided radius is equals to {Result}cm.")