session_price = 5.00
member = input("Are you a member? (yes/no): ").lower()

if member == "yes":
    category = input("Are you a senior citizen, adult, or child? ").lower()

    if category == "senior citizen":
        price = session_price * 0.50
    elif category == "adult":
        price = session_price * 0.90
    elif category == "child":
        price = session_price * 0.75
    else:
        price = session_price
else:
    price = session_price

print("Session price: price: $", price)
