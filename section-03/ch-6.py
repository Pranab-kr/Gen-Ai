# You're building a ticket info system for a railway app.
# Based on seat type, show its features.

# Task:

# * Input: "sleeper" , "AC" , "general" , "luxury"

# * Match using match-case
# * Unknown — show: "Invalid seat type"

seat_type = input("Enter seat type (sleeper, AC, general, luxury): ").lower()
match seat_type:
    case "sleeper":
        print("Sleeper: Basic comfort, non-AC")

    case "ac":
        print("AC: Comfortable, air-conditioned")

    case "general":
        print("General: Basic seating, no reservation")

    case "luxury":
        print("Luxury: premium comfort, AC, meals included")

    case _:
        print("Invalid seat type")
