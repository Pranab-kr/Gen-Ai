# Dictionary (is like object in JavaScript)

chai_order = dict(type="chai", size="medium", sugar_level="half")

print(chai_order)

chai_recipe = {}
chai_recipe["tea"] = "black tea"
chai_recipe["spices"] = ["cinnamon", "cardamom", "ginger"]
chai_recipe["milk"] = "whole milk"

print(chai_recipe)

del chai_recipe["milk"]
print(chai_recipe)

#membership test
print(f"Is sugar_level in chai_order? {'sugar_level' in chai_order}")

chai_order = {"type": "ginger", "size": "small", "sugar_level": "full"}

# print(chai_order.keys())
# print(chai_order.values())
# print(chai_order.items())

last_item = chai_order.popitem()
print(f"Last item removed: {last_item}")

extra_spices = ["cloves:1/2 tsp", "black pepper:1/4 tsp"]

print(f"Before update: {chai_recipe}")
chai_recipe.update({"spices": extra_spices})
print(f"After update: {chai_recipe}")

customer_note = chai_order.get("water", "NO note found") # Using get() to avoid KeyError
print(customer_note)
