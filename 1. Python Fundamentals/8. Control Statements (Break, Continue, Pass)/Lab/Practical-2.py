"""
Write a Python program to stop the loop once 'banana' is found using
the break statement.
"""

list1 = ['apple', 'cherry', 'banana', 'mango']

for i in list1:
    if i in 'banana':
        continue
    print(i)