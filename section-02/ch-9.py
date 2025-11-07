# set
essential_spices = {"cinnamon", "nutmeg", "ginger"}
optional_spices = {"clove", "allspice", "nutmeg"}

all_spices = essential_spices | optional_spices

print(all_spices)

common_spices = essential_spices & optional_spices

print(common_spices)

only_in_essential = essential_spices - optional_spices
print(only_in_essential)

#membership test
print(f"is clove an optional? {'clove' in optional_spices}")
