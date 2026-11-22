firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")

print(firstname + " is " + str(len(firstname)) + " characters long.")
print(surname + " is " + str(len(surname)) + " characters long.")
print(firstname + " " + surname + " is " + str(len(firstname) + len(surname)) + " characters long.")