sales = float(input("Enter Sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
        print(bonus)
    else:
        bonus = sales * 0.15
        print(bonus)
print("Invalid Sales Amount")


#Version 2

sales = float(input("Enter Sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Bonus is $ ", bonus)