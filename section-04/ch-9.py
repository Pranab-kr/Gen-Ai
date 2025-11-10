# Using Dictionaries Instead of Repeated Cases

users = [
    {"id": 1, "total": 150, "cupon": "DISCOUNT10"},
    {"id": 2, "total": 200, "cupon": "DISCOUNT15"},
    {"id": 3, "total": 50, "cupon": "DISCOUNT5"}
  ]

discounts = {
  "DISCOUNT10": (0.2, 0),
  "DISCOUNT15": (0.3, 0),
  "DISCOUNT5": (0.1, 0)
}

for user in users:
  percent, fixed = discounts.get(user["cupon"], (0, 0))
  discount_amount = user["total"] * percent + fixed
  final_total = user["total"] - discount_amount
  print(f"User {user['id']} final total: {final_total}")
