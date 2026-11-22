entry = input("Enter some data: ")
name = input("Enter your name: ")

while entry == "":
    print("Error: no data was entered.")
    entry = input("Enter some data: ")

print("Thank you ", name, "your comment has been posted.")
