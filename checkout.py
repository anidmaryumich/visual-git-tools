def calculate_total(prices, tax_rate=0.06):
    subtotal = sum(prices)
    total = subtotal * (1 + tax_rate)
    return total


print("DEBUG total w/ tax:", total)
