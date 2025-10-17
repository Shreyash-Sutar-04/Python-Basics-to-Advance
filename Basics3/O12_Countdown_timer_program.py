import time

# This won't show countdown to see it 
time.sleep(15)
print("Hey There Thank you for patience!")
  
# This is how you will notice the time period!
my_time = int(input("Enter the time in seconds :"))
my_time = my_time+1 #This is because of start the countdown from user input itself
for x in reversed(range(1,my_time)):
    time.sleep(1)
    print(x)
print("YOU MADE IT!")

# Another technique to print reverse countdown is 
Time = int(input("Enter your time period in seconds : "))
for i in range(Time,0,-1):
    time.sleep(1)
    print(i)
# range(start,end,step) now in this case we have considered the step as -1 
# so here everytime the countdown is minimizin by 1