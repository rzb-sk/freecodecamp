print("Welcome to the pay calculator!")
print("Please enter the following details!")

hours_worked = input("Enter the hours worked: ")
hourly_rate = input("Enter the hourly rate: $")
pay = float(hours_worked) * float(hourly_rate)

print("Pay:",pay,"USD")