total = 0
number_of_items = int(input("How many items are there?: "))
while number_of_items < 0:
    number_of_items = int(input("How many items are there?: "))
for i in range(number_of_items):
    price_of_items = float(input("Price of item: "))
    total += price_of_items

if total > 1000:
    total *= 0.9

print("Total price for {} items is ${:.2f}".format(number_of_items, total))