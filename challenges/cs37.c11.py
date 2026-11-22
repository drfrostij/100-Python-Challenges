def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3


side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))
print("The perimeter is:", triangle_perimeter(side1, side2, side3))
