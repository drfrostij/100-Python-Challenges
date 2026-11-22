def add_num(num1, num2):
    answer = num1 + num2
    return answer


def subtract_num(num1, num2):
    answer = num1 - num2
    return answer


num1 = int(input("Enter integer 1: "))
num2 = int(input("Enter integer 2: "))
menu_option = input("Enter menuOption (add/subtract): ").lower()

if menu_option == "add":
    answer = add_num(num1, num2)
else:
    answer = subtract_num(num1, num2)

print(answer)
