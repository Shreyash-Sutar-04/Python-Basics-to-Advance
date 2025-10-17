temp = int(input("Enter the temprature:"))
weather = "Hot" if temp>=28 else "Good to GO!"
print(f"The weather is kinda {weather} today!")

role = input("Enter your role:")
status = "Full_Access" if role == "Admin" else "Limited_Access"
print(f"As per your role you have {status}.")