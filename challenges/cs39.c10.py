name_to_find = input("Enter a name to search for: ")

file = open("names.txt", "r")
name_exists = False

for line in file:
    if line.strip() == name_to_find:
        name_exists = True
        break

file.close()

if name_exists:
    print(name_to_find, "exists in the file.")
else:
    print(name_to_find, "does not exist in the file.")
