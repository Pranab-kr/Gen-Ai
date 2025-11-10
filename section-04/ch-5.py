# You're preparing an order summary with customer names
# and their total bill.
# Task:

# « Use two lists: one for names and one for bills.

# « Print: "[Name] paid Rs.[amount]"

names =  ["Alice", "ram", "pkm", "sita"]
bills = [50, 30, 70, 40]

for name, bill in zip(names, bills):
    print(f"{name} paid ₹{bill}")
