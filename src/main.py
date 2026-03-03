def sum_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: inputs must be numbers"
    return a + b

print(sum_numbers(5, 3))