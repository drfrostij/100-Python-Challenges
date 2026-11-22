entry = input("Enter an integer: ")

while not entry.lstrip("-").isdigit():
    print("Invalid input. Please enter an integer.")
    entry = input("Enter an integer: ")

number = int(entry)
print("You entered", number)
