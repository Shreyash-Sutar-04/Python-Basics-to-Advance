# A conditional expression lets you write an if-else statement in a single line — it’s a compact way to choose between two values based on a condition.
#  value_if_true if condition else value_if_false
#  Formula X if condition else Y
Age = int(input("Enter Your Age : "))
num1 = int(input("Enter Number 1 "))
num = int(input("Enter the Number 2: "))

print(f" The Number 2 is {"Even" if num%2 == 0 else "Odd"}")

result = "Positive" if num>0 else "Negative"
print(f"The Number2 is : {result}")

max_num = num1 if num1>num else num
print(f"maximum number is : {max_num}")

min_num = num1 if num1<num else num
print(f"Minimum number is: {min_num}")

status = "Adult" if Age>=18 else "Minor"
print(f"You are {status}.")



