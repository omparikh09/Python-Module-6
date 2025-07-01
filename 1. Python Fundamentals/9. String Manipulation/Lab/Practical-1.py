"""
Write a Python program to demonstrate string slicing.
"""

# Get input form user in string
text = input("Enter a text :- ")

print()

# Slice from index 0 to 5
print("Slice from index 0 to 5 text[0:6]:", text[0:6])  

# Slice from index 6 to the end
print("Slice from index 6 to the end text[6:]:", text[6:])   

# Slice entire string
print("Slice entire string text[:]:", text[:])

# Slice with step of 2
print("Slice with step of 2 text[::2]:", text[::2])  

# Slice from end (last 3 characters)
print("Slice from end (last 3 characters) text[-3:]:", text[-3:]) 

# Reverse the string using slicing
print("Reversed string:", text[::-1])
