file = open("hello.txt", "r")

file.readline()
second_line = file.readline()

file.close()
print(second_line.strip())
