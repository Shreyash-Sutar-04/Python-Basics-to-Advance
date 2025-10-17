#Python calculator

operator = input("Enter the operator(+,-,*,/) :")
num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))

if operator == "+":
    print(f"The Addition is {num1+num2}")
elif operator == "-":
    print(f"The Substraction is {num1-num2}")
elif operator == "*":
    print(f"The Multiplication is {num1*num2}")
elif operator == "/":
    print(f"The Division is {num1/num2}")
else:
    print(f"The {operator} is not valid operation!!!!!")
