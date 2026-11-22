snickerbar = 0.75

numberofbars = int(input("Enter the number of snicker bars you want to buy: "))

totalcost = snickerbar * numberofbars

print("The total cost of", numberofbars, "snicker bars is $", totalcost)

payment = float(input("Enter the amount you are paying: "))

change = payment - totalcost

print("Your change is $", change)