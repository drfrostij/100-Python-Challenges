option = int(input("Enter a menu option from 1 to 4: "))

while option < 1 or option > 4:
    option = int(input("Invalid option. Enter a number from 1 to 4: "))

print("You selected option", option)
