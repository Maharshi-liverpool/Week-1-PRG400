feedback = [
    "Good service",
    "Excellent staff and management",
    "Nice",
    "The product quality was amazing",
    "Ok"
]

# Filter feedback with >= 20 characters
long_feedback = list(filter(lambda msg: len(msg) >= 20, feedback))

# Convert to lowercase
lowercase_feedback = list(map(lambda msg: msg.lower(), long_feedback))

print("Original feedback:", feedback)
print("Filtered feedback (>= 20 chars):", long_feedback)
print("Lowercased feedback:", lowercase_feedback)