hours = [30, 42, 53, 37, 44, 60]

# Filter employees who worked at least 40 hours
eligible_hours = list(filter(lambda h: h >= 40, hours))

# Convert to overtime
overtime_hours = list(map(lambda h: h - 40, eligible_hours))

print("Original hours:", hours)
print("Eligible hours (>= 40):", eligible_hours)
print("Overtime hours:", overtime_hours)