temp = int(input("Enter the temprature today :"))
is_sunny = True

if temp>=28 and is_sunny:
    print("The sun is pissing fire!")
    print("You better sit home!")
elif temp<=0 and is_sunny:
    print("Its damn cold!")
    print("Just sleep bro!")
elif 28>temp>0 and is_sunny:
    print("Perfect time to go outside!")
elif temp>=28 and not is_sunny:
    print("Go but take an umbrella with you!")
