file = open("about_me.txt", "w")

for i in range(5):
    fact = input("Enter something about yourself: ")
    file.write(fact + "\n")

file.close()
