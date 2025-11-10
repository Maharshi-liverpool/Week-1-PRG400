scores = [44, 59, 77, 83, 93, 62, 50, 81]

# Filter passing scores
passing_scores = list(filter(lambda s: s >= 50, scores))

# Convert to letter grades
grade_map = list(map(
    lambda s: 
        'A' if s >= 90 else
        'B' if s >= 80 else
        'C' if s >= 70 else
        'D' if s >= 60 else
        'E',
    passing_scores
))

print("Original scores:", scores)
print("Passing scores:", passing_scores)
print("Letter grades:", grade_map)