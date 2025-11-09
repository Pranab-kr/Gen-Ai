# A tea stall offers different prices for different cup sizes.
# Write a program that calculates the price based on size.

# Task:
# « Input: “small”, "medium", "large"
# « Small — 10, Medium — 15, Large — 20
# « If invalid: show "Unknown cup size"

cup_size = input("Enter cup size (small, medium, large): ").lower()

if cup_size == "small":
    print("Price: 10")
elif cup_size == "medium":
    print("Price: 15")
elif cup_size == "large":
    print("Price: 20")
else:
    print("Unknown cup size")
