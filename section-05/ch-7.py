# nonLocal Keyword in Python


def update_order():
    chai_type = "Masala Chai"
    print(f"Initial chai type: {chai_type}")

    def kitchen():
        nonlocal chai_type
        chai_type = "Ginger Chai"
        print(f"Chai prepared in kitchen: {chai_type}")

    kitchen()
    print(f"Chai served: {chai_type}")


update_order()

# Global Keyword in Python

chai_type = "Green Tea"
print(f"Initial chai type at front desk: {chai_type}")


def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Lemon Chai"
        print(f"Chai prepared in kitchen: {chai_type}")

    kitchen()


front_desk()
print(f"Chai available at front desk: {chai_type}")
