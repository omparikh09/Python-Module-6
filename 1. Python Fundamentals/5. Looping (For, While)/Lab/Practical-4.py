"""
Print this pattern using nested for loop:
markdown
Copy code
*
* *
* * *
* * * *
* * * * *
"""

rows = int(input("Enter a number of rows you went to print :- "))
for i in range(1, rows+1):
    for j in range(i):
        print("*",end=" ")
    print()
    
