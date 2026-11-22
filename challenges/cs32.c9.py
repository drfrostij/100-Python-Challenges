initalvelocity = float(input("Enter the initial velocity (m/s): "))
finalvelocity = float(input("Enter the final velocity (m/s): "))
timetaken = float(input("Enter the time taken (s): "))

acceleration = (finalvelocity - initalvelocity) / timetaken

print("The acceleration is:", acceleration, "m/s^2")