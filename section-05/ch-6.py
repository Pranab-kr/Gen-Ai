# scopes in Python functions


def serve_chai():
    chai_type = "Masala Chai"  # Local scope
    print(f"Serving {chai_type}")


chai_type = "Green Tea"  # Global scope
serve_chai()
print(f"Outside function, chai_type is: {chai_type}")


# Demonstrating scope with nested functions


def chai_counter():
    chai_ordered = "lemon"
    print(f"Chai ordered: {chai_ordered}")

    def print_order():
        chai_ordered = "Ginger"  # Accessing enclosing scope
        print(f"Serving chai number: {chai_ordered}")

    print_order()  # Call the nested function


chai_ordered = "Cardamom"  # Global scope
chai_counter()

print(f"Global chai_ordered before function call: {chai_ordered}")
