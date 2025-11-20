# Your shop adds a 10% VAT on every order.
# You want this to be consistent and traceable.
# Task:

# » Write add_vat(price, vat_rate)

# « Use it to compute final prices for 3 orders


def add_vat(price, vat_rate):
    vat_amount = price * (vat_rate / 100)
    final_price = price + vat_amount
    return final_price


order_prices = [100, 250, 400]
vat_rate = 10

for i, price in enumerate(order_prices, 1):
    print(f"Final price for order {i}: {add_vat(price, vat_rate)}")
