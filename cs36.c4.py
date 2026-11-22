total = 0
number = int(input("Enter a number (0 to stop): "))

while number != 0:
    total += number
    print("Accumulated total:", total)
    number = int(input("Enter a number (0 to stop): "))

print("Final total:", total)
