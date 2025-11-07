# the value/number is not mutable, the reference is changed to point to a new value in memory

sugar_amount = 10

print(f"First sugar amount: {sugar_amount}")

sugar_amount = 20

print(f"Second sugar amount: {sugar_amount}")

print(f"Id of first sugar amount: {id(10)}")
print(f"Id of second sugar amount: {id(20)}")
