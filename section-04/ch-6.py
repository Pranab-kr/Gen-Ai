# You want to simulate tea heating.

# It starts at 40°C and boils at 100°C.

# Task:
# * Use a while loop.
# « Increase temperature by 15 until it reaches or exceeds 100
# « Print each temperature step.

temp = 40
while temp < 100:
    print(f"Current temperature: {temp}°C")
    temp += 15
print("Tea has boiled at 100°C!")
