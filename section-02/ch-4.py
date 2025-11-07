is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting bool to int (True as 1, False as 0)

print("Total actions (int + bool):", total_actions)

milk_present = 0
print(f"Is milk present? {bool(milk_present)}") # downcasting int to bool (0 as False, non-zero as True )

water_hot = True
tea_added = False

can_server_tea = water_hot and tea_added # logical AND
print(f"Can serve tea? {can_server_tea}")

print(f"Water hot or tea added? {water_hot or tea_added}") # logical OR# Booleans
