"""

"""

# Define a string
text = "  hello, Python World!  "

# Use various string methods
print("Original string:", repr(text))

# Strip whitespace
strip = text.strip()
print("After strip():", repr(strip))

# Convert to uppercase
upper = strip.upper()
print("Uppercase:", upper)

# Convert to lowercase
lower = strip.lower()
print("Lowercase:", lower)

# Capitalize the first letter
capitalized = strip.capitalize()
print("Capitalized:", capitalized)

# Replace a word
replaced = strip.replace("Python", "Java")
print("After replace():", replaced)

# Split the string into a list
split = strip.split()
print("After split():", split)

# Check if the string starts with "hello"
print("Starts with 'hello'? :", strip.startswith("hello"))

# Count occurrences of 'o'
print("Number of 'o's:", strip.count('o'))
