#Compund Interest calculator

"""
A = final amount
P = Initial Principal Balance
r = Initial rate
t = Nuber of time period elipsed!
Formula = A = P(1+r/n)^t
"""
principal = 0
rate = 0
time_period = 0

while principal <= 0:
    principal = float(input("Enter your principal amount (in Rupees): "))
    if principal <= 0:
        print("Principal can't be less than or equal to zero.")

while rate <= 0:
    rate = float(input("Enter your rate (in percentage): "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero.")

while time_period <= 0:
    time_period = float(input("Enter your time period (in years): "))
    if time_period <= 0:
        print("Time period can't be less than or equal to zero.")

print("\n✅ Input Summary:")
print(f"Principal: ₹{principal}")
print(f"Rate: {rate}%")
print(f"Time Period: {time_period} years")

print("Therefore The Compound interest will be as following:")
print(f"The compound interest for Principal {principal},rate{rate} and time period of {time_period} will be:")
result = principal * pow((1 + rate/100), time_period)
print(round(result,2))
#or
print(f"{result: .2f}")