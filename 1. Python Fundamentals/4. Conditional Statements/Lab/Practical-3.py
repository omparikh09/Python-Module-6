"""
Write a Python program to calculate grades based on percentage using
if-else ladder
"""

percentage = float(input("Enter your percentage :- "))

if percentage >= 90:
    print("Grade : A+")
elif percentage >= 80:
    print("Grade : A")
elif percentage >= 70:
    print("Grade : B")
elif percentage >= 60:
    print("Grade : C")
elif percentage >= 50:
    print("Grade : D")
elif percentage >= 40:
    print("Grade : E")
else:
    print("Grade : Fail")
