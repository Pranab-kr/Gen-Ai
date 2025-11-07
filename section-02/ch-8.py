# Working with Lists in Python like arrays

ingredients = ["Cumin", "Coriander", "Cardamom", "Ginger"]
ingredients.append("Cloves")

print(f"Updated ingredients list: {ingredients}")
ingredients.remove("Ginger")
print(f"Ingredients list after removing Ginger: {ingredients}")


spice_options = ["Black Pepper", "Cinnamon", "Nutmeg"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai ingredients: {chai_ingredients}")

chai_ingredients.insert(2, "tea leaves") # Inserting tea leaves adding at index 2
print(f"Chai ingredients after adding tea leaves: {chai_ingredients}")

lastadded_spice = chai_ingredients.pop() # Removing last added spice
print(f"Removed last added spice: {lastadded_spice}")
print(f"Chai ingredients after removing last added spice: {chai_ingredients}")

# reversing the list
chai_ingredients.reverse()
print(f"Chai ingredients in reverse order: {chai_ingredients}")

# sorting the list
chai_ingredients.sort()
print(f"Chai ingredients sorted alphabetically: {chai_ingredients}")

# max & min
sugar_levels = [5, 10, 3, 8, 2]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")


# Operator overloading and bytearray in python
base_liquids = ["water", "milk"]
extra_falvor = ["vanilla"]

full_liquids = base_liquids + extra_falvor
print(f"Full liquids list: {full_liquids}")

strong_brew = extra_falvor * 3
print(f"Strong brew flavoring: {strong_brew}")

# Working with bytearray

raw_spice_data = bytearray(b'CINNAMON')
print(f"Raw spice data: {raw_spice_data}")

raw_spice_data = raw_spice_data.replace(b'CINNAMON', b'CARDAMOM')

print(f"Updated spice data: {raw_spice_data}")
