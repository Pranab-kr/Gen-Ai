# A local cafe wants a program that suggests a snack.
# If a customer asks for cookies or samosa, it confirms the order.
# Otherwise, it says it's not available.

# Task:
# « Take snack input
# * If it's "cookies" or "samosa" , confirm the order
# « Else, show unavailability

user_input = input("Welcome to the cafe! What snack would you like to order? ").lower()

if user_input == "cookies" or user_input == "samosa":
    print(f"Great choice! Your order for {user_input} has been placed.")
else:
    print(f"Sorry, we don't have {user_input} available right now.")
