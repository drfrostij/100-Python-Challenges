taxable_income = float(input("Enter your taxable income: "))

if taxable_income >= 30000:
    taxable_income_over_threshold = taxable_income - 30000
    taxes = 4500 + (taxable_income_over_threshold * 0.28)
else:
    taxes = taxable_income * 0.15

print("Tax:", taxes)
