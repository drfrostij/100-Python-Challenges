def apply_discount(price):
    return price * 0.90


price = float(input("Enter the price: "))
discounted_price = apply_discount(price)
print("Discounted price:", discounted_price)
