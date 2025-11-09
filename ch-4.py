# You're building a smart thermostat alert system:
# «If the device_status is "active"
# * And temperature > 35 — Warn: "High temperature alert!"
# « Else: "Temperature normal"
# « If device is off — "Device is offline"

device_status = input("Enter device status (active/off): ").lower()


if device_status == "active":

    temp = float(input("Enter current temperature: "))
    if temp > 35:
        print("High temperature alert!")
    else:
        print("Temperature normal")

elif device_status == "off":
    print("Device is offline")

else:
    print("Unknown device status")
