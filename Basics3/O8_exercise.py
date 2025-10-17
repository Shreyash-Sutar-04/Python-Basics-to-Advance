#Let user enter number between 1 to 10

num =  int(input("Enter thr number from 1 to 10 : "))
while num<1 or num>10:
    print("Invalid number crteria!")
    num =  int(input("Enter thr number from 1 to 10 : "))
print(f"You chose {num}")