print("Electricity Bill Estimator.")
cents = int(input("Cents per kWh: "))
daily_use = int(input("Daily use in kWh: "))
billing_days = int(input("Billing Days: "))
daily_price = cents * daily_use
total_price = daily_use * billing_days
print(total_price)