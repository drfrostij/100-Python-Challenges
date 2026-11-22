password = input("Enter a password: ")

while len(password) < 10:
    print("Password must be at least 10 characters.")
    password = input("Enter a password: ")

print("Password accepted.")
