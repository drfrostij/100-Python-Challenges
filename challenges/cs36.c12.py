correct_username = "elmo"
correct_password = "blue"
attempts = 0

while attempts < 3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    attempts += 1

    if username == correct_username and password == correct_password:
        print("Login successful.")
        break

    print("Incorrect username or password.")
else:
    print("You are locked out.")
