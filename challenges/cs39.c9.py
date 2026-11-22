file = open("users.txt", "w")
file.write("Username\nPassword\n")
file.close()

username = input("Enter a username: ")
password = input("Enter a password: ")

file = open("users.txt", "a")
file.write(username + "\n" + password + "\n")
file.close()
