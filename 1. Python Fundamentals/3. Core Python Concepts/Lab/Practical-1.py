"""
Write a Python program to demonstrate the creation of variables and different data types.
"""

# Integer Datatype
age = 21

# Float Datatype
height = 5.4

# String Datatype
name = "Om"

# Boolean Datatype
student = True 

# List Collection Datatype
subject = ["Hindi","English","Math","Science","History"]

# Tuple Collection Datatype
roll_no = (12,29,14,64)

# Dictionary Collection Datatype
student_detail = {
    "Name" : "Om",
    "Age" : "21",
    "Subject" : "Python",
}

# Set Collection Datatype
unique_numbers = {1, 3, 4, 2, 1}

print(f"Name :- {name} ->\n",type(name))
print(f"\nAge :- {age} ->\n",type(age))
print(f"\nHeight :- {height} ->\n",type(height))
print(f"\nIs Student :- {student} ->\n",type(student))
print(f"\nSubject :- {subject} ->\n",type(subject))
print(f"\nRoll No :- {roll_no} ->\n",type(roll_no))
print(f"\nStudent Details :- {student_detail} ->\n",type(student_detail))
print(f"\nUnique Numbers :- {unique_numbers} ->\n",type(unique_numbers))