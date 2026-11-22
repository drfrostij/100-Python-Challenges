age = int(input("Enter your age: "))

if age > 65:
    print("You are eligible for a senior citizen discount.")
elif age <= 16:
    print("You are eligible for a child discount.")
else:
    print("You are not eligible for a discount.")
