"""
Write a Python program to apply the map() function to square a list of numbers.
"""

# Define the list of numbers
numbers = [10, 20, 30, 40, 50]

# Use map() with a lambda function to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Squared list:", squared_numbers)
