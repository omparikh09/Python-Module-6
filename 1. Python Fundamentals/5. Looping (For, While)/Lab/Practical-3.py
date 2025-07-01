"""
Write a Python program to find a specific string in the list using a simple
for loop and if condition
"""

l1 = ['apple', 'banana', 'cherry', 'orange', 'mango']

search = input("Enter for Search a string :- ")

found = False

for i in l1:
    if i in search:
        print(f"'{search}' found in the list.")
        found = True
        break
    
if search not in l1:
    print(f"'{search}' not found in the list.")