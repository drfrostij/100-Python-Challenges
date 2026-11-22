file = open("about_me.txt", "r")

while True:
    line = file.readline()

    if line == "":
        break

    print(line.strip())

file.close()
