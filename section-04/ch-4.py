# You're creating a tea menu board.
# Each item must be numbered.
# Task:
# + Use enumerate() to print menu items with numbers.

menu_items = ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Lemon Tea", "Green Tea"]

for index , item in enumerate(menu_items, start=1):
    print(f"{index}. {item}")
