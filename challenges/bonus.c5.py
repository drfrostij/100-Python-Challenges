in_a_hurry = input("Are you in a hurry? (yes/no): ").lower()

if in_a_hurry == "yes":
    print("Request a cab")
else:
    destination_downtown = input("Is the destination downtown? (yes/no): ").lower()

    if destination_downtown == "yes":
        print("Coach")
    else:
        print("Train/Bus")
