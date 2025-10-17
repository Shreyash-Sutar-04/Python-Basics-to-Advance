#if = Do some code only if some condition is True 
# else = do something else

age = int(input("Enter Your age :"))

if age>=100:
    #After if the indetention is required 
    print("Bro you should be in coffin!")
# We can check more conditions before reaching else statement
elif age<=0:
    print("I asked about age not account balance")
elif age>=18:
    print("You are an adult!")   
else :
    print("Go get ur parents!!!!")
