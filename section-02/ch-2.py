# the set object is mutable, so the reference remains the same even after modifications

spice_mix = set()

print(f"Initial spice mix: {id(spice_mix)}")

spice_mix.add("cinnamon")
spice_mix.add("nutmeg")
print(f"Spice mix after additions: {id(spice_mix)}")

print(spice_mix)
