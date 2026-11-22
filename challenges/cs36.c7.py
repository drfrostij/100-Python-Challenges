correct_name = "Eric"
attempts = 0

while attempts < 3:
    name = input("Enter the name: ")
    attempts += 1

    if name == correct_name:
        print("Correct name.")
        break

    print("Incorrect name.")
else:
    print("You have used all three attempts.")
