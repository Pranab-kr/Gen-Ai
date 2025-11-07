# Intergers

black_tea_price = 15
green_tea_price = 20

total_price = black_tea_price + green_tea_price
print("Total price:", total_price)

price_difference = green_tea_price - black_tea_price
print("Price difference:", price_difference)

milk_liters = 7
sugar_spoons = 3

sugar_per_liter = sugar_spoons / milk_liters
print("Sugar spoons per liter of milk:", sugar_per_liter)

total_tea_bag = 7
pots = 4
tea_bags_per_pot = total_tea_bag // pots # floor division, does not return decimal values
print(f"Tea bags per pot: {tea_bags_per_pot}")

total_cadamon_pods = 29
people = 8
leftover_pods = total_cadamon_pods % people # modulus operator
print(f"Leftover cardamom pods: {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavor_strength = base_flavor_strength ** scale_factor # exponentiation operator, 2 * 2 * 2
print(f"Powerful flavor strength: {powerful_flavor_strength}")
