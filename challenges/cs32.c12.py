numberone = int(input("Enter the first number: "))
numbertwo = int(input("Enter the second number: "))

original_numberone = numberone  # Store the original value of numberone for display

for i in range(1, numbertwo + 1):
    numberone = numberone * numberone

print(" the exponent of", original_numberone, "to the power of", numbertwo, "is", numberone)