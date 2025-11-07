# String

chai_type = "Green Tea"
customer_name = "Onisuna"

print(f"Customer {customer_name} ordered a cup of {chai_type}.")

chai_des = "Aromatic and bold"
print(f"First word: {chai_des[0:8]}")
print(f"First word: {chai_des[:4]}")

print(f"last word: {chai_des[9:]}")
print(f"last word: {chai_des[:8:2]}")

#Reverse a string
print(f"Reversed string: {chai_des[::-1]}")

label_name = "Chai Latte"
print(label_name.upper())
print(label_name.lower())

#Encording and Decoding
sample_text = "Chai is great!"
encoded_text = sample_text.encode("utf-8",)
print(f"Encoded text: {encoded_text}")
decoded_text = encoded_text.decode("utf-8")
print(f"Decoded text: {decoded_text}")
