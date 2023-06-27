# Set the menu
menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70),
        ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]

# Display the menu
print("The Menu is as follows:")
print()
for i in range(len(menu)):
    s_no = i+1
    item = menu[i][0]
    price = menu[i][1]
    print(f"{s_no}. {item}: {price}")
print()

user_input = []

# Continuously ask the user for input until they decide to stop by returning empty string

while True:
    ele = [int(c) for c in input(
        "From the menu displayed above, kindly enter the serial number of the desired item and its quantity as space separated values: ").split()]
    if ele == []:
        break
    user_input += [ele]
print()

# Remove duplicates and calculate the total quantity for each item
item_totals = {}
for item, quant in user_input:
    if item in item_totals:
        item_totals[item] += quant
    else:
        item_totals[item] = quant

# Sort the items by serial number
sorted_items = sorted(item_totals.items(), key=lambda x: x[0])

# Print the bill
tot_price = 0
tot_items = 0
for item, quant in sorted_items:
    item_name = menu[item-1][0]
    price = quant * menu[item-1][1]
    tot_items += quant
    tot_price += price
    print(f"{item_name}, {quant}, Rs {price}")
print()
print(f"TOTAL, {tot_items} items, Rs {tot_price}")
