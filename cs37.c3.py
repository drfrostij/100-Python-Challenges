def compare_to_ten(number):
    if number > 10:
        print(number, "is greater than 10")
    elif number < 10:
        print(number, "is less than 10")
    else:
        print(number, "is equal to 10")


number = int(input("Please enter a number: "))
compare_to_ten(number)
