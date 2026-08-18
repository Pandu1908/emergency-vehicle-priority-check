vehicle = input("Enter vehicle type: ").lower()

if vehicle == "ambulance":
    print("🚑 EMERGENCY!")
    print("🟢 Give priority to ambulance.")
elif vehicle == "fire":
    print("🔥 Give priority to fire vehicle.")
else:
    print("🚗 Normal traffic rules apply.")
