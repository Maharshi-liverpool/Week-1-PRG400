salaries = {
    "Nishant": 55000,
    "Bob": 65000,
    "Bikesh": 72000,
    "Adesh": 58000,
    "Anup": 90000
}

# Filter employees with salary >= 60000
filtered_employees = dict(filter(lambda item: item[1] >= 60000, salaries.items()))

#Apply 5% raise using map()
raised_salaries = dict(map(lambda item: (item[0], round(item[1] * 1.05, 2)), filtered_employees.items()))

print("Original salaries:", salaries)
print("Filtered employees (>= $60,000):", filtered_employees)
print("After 5% raise:", raised_salaries)