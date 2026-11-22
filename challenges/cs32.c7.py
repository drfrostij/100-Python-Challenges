num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
action = input("Enter the action (add, subtract, multiply, divide): ")

if action == "add":
    result = float(num1) + float(num2)
    print("The result of addition is:", result)
elif action == "subtract":
    result = float(num1) - float(num2)
    print("The result of subtraction is:", result)
elif action == "multiply":
    result = float(num1) * float(num2)
    print("The result of multiplication is:", result)
elif action == "divide":
    if float(num2) != 0:
        result = float(num1) / float(num2)
        print("The result of division is:", result)
    else:
        print("division by zero is not allowed.")
else:
    print("Error: Invalid action.")