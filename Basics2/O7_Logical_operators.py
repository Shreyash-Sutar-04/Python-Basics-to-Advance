# Logical Operators - Evaluates the multiplr conditions(or,and,not)
#                     or - At least one condition must be true
#                     and - Both conditions must be true  
#                     not - Inverts the condition(not False,Not Ture)      

temp = 36
is_raining =False

if temp >35 or temp<0 or is_raining:
    print("The outdoor event is cancelled!")
else:
    print("The outdoor event is still scheduled!")


charge = int(input("Enter Smartphone battery percentage: "))
is_battery_saver_on = input("Is battery saver on? (True/False): ").lower() == "true"

if charge < 20 and is_battery_saver_on:
    print("Need to put on charging!")
elif 30 < charge < 50:
    print("You might need to charge in a few minutes.")
elif charge > 80:
    print("Not necessarily need to charge it!")
else:
    print("Good to go man!")
