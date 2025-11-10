# Walrus

# The walrus operator (:=) allows you to assign values to variables as part of an expression.
# This can help to reduce redundancy and improve readability in certain situations.

# Example without walrus operator
value = 13
# reminder = value % 5

# if reminder:
#     print(f"{value} is not divisible by 5, remainder is {reminder}")

# Example with walrus operator
if (reminder := value % 5):
    print(f"{value} is not divisible by 5, remainder is {reminder}")


size = ["small", "medium", "large", "extra large", "jumbo"]

if (n := input("Enter size (Small/Medium/Large/Extra Large/Jumbo): ").lower()) in size:
    print(f"Preparing a {n} chai for you.")
