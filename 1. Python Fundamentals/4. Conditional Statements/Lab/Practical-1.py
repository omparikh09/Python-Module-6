"""
Write a Python program to find greater and less than a number using
if else.
"""

n1 = int(input("Enter a number1 :- "))
n2 = int(input("Enter a number2 :- "))

if n1 < n2:
    print(f"{n1} Is Greater Than {n2}")
elif n1 > n2:
    print(f"{n1} Is Less Than {n2}")
else:
    print(f"{n1} Is Equal To {n2}")