def in_range(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound


number = float(input("Enter a number: "))
lower_bound = float(input("Enter the lower bound: "))
upper_bound = float(input("Enter the upper bound: "))

if in_range(number, lower_bound, upper_bound):
    print("The number is in range.")
else:
    print("The number is not in range.")
