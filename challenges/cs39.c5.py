names = ["Sarah", "Rickie", "Rob", "Charlie", "Daisy"]

file = open("names.txt", "w")

for name in names:
    file.write(name + "\n")

file.close()
