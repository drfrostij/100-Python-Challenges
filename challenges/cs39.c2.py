name = input("Enter your name: ")

file = open("hello.txt", "a")
file.write("\n" + name)
file.close()
