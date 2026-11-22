import random

names = []
number_of_names = random.randint(1, 10)

print("You need to enter", number_of_names, "names.")

for i in range(number_of_names):
    name = input("Enter a name: ")
    names.append(name)

print(names)
