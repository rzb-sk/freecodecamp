hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hours > 40:
    # print('Overtime Pay')
    reg_pay = hours * rate # regular pay calculation
    over_pay = (hours - 40) * (rate * 0.5) # overtime pay calculation
    # print(reg_pay, '+', over_pay)
    over_pay = reg_pay + over_pay # Adding the overtime pay to the regular pay
    print(over_pay)
else:
    print('Regular Pay')
    reg_pay = hours * rate # regular pay calculation
    print(reg_pay)