# use of return statement in functions

# You sell different chai sizes.
# Instead of writing formulas everywhere, create a function.
# Task:

# * Write calculate_bill(cups, price_per_cup)

# « Return total bill

# « Use this function for multiple orders


def calculate_bill(cups, price_per_cup):
    total_bill = cups * price_per_cup
    return total_bill


calculate_bill_1 = calculate_bill(3, 5)
print(f"Total bill for order 1 is: {calculate_bill_1}")

calculate_bill_2 = calculate_bill(3, 8)
print(f"Total bill for order 2 is: {calculate_bill_1}")
