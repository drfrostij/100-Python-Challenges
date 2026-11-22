def cook(desired_temperature):
    toast_temperature = 0

    while toast_temperature < desired_temperature:
        print("Heat is on")
        toast_temperature = float(input("Enter the toast temperature: "))

    print("Heat is off")


while True:
    switch = input("Enter 'pressed' to cook: ").lower()

    if switch == "pressed":
        cook(60)
