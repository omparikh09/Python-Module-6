"""
Write a Python program that filters out even numbers using the filter() function.
"""

# Define the list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() with a lambda to keep only odd numbers (i.e., filter out even ones)
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Print the result
print("After filtering out even numbers:", odd_numbers)
