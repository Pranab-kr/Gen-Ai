# tuples are immutable sequences, typically used to store collections of heterogeneous data, not changeable after creation

masala_spices = ("Cumin", "Coriander", "Cardamom")

(spice1, spice2, spice3) = masala_spices # Unpacking the tuple into individual variables

print(f"Spice 1: {spice1}, Spice 2: {spice2}, Spice 3: {spice3}")
ginger_ratio, cardamom_ratio = 2, 1 # Initial ratios

print(f"Ginger to Cardamom Ratio: {ginger_ratio}:{cardamom_ratio}")

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio # Swapping the ratios

print(f"After swapping - Ginger to Cardamom Ratio: {ginger_ratio}:{cardamom_ratio}")

# membership test
print(f"Is 'Cumin' in masala_spices? {'Cumin' in masala_spices}")
print(f"Is 'Turmeric' in masala_spices? {'Turmeric' in masala_spices}")
