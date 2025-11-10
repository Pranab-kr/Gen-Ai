# Some chai flavors are out of stock.

# You want to skip those and stop entirely if
# someone requests a restricted flavor.
# Task:

# « Skip if flavor is "Out of Stock"

# * Break if flavor is "Discontinued"

flavors = ["Masala", "Vanilla", "Out of Stock", "Cardamom", "Discontinued", "Ginger"]

for flavor in flavors:
    if flavor == "Out of Stock":
        continue
    if flavor == "Discontinued":
        print("This flavor has been discontinued. Stopping orders.")
        break
    print(f"Preparing your {flavor} chai.")
