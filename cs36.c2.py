correct_name = "Eric"
attempts = 0
name = input("Enter the name: ")

while name != correct_name:
    attempts += 1
    name = input("Incorrect. Enter the name again: ")

attempts += 1
print("Correct name entered after", attempts, "attempt(s).")
