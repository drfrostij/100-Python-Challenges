lamp_plugged_in = input("Is the lamp plugged in? (yes/no): ").lower()

if lamp_plugged_in == "yes":
    bulb_burned_out = input("Is the bulb burned out? (yes/no): ").lower()

    if bulb_burned_out == "yes":
        print("Replace bulb")
    else:
        print("Repair lamp")
else:
    print("Plug in lamp")
