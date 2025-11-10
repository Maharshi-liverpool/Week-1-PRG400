prices =  [25, 60, 120, 45, 80, 30, 200]

# Filter products priced >= $50
filtered_prices = list(filter(lambda p: p >= 50, prices))

# Apply 10% discount
discounted_prices = list(map(lambda p: p * 0.9, filtered_prices))

print("Original prices:", prices)
print("Filtered prices (>= $50):", filtered_prices)
print("Discounted prices (10% off):", discounted_prices)