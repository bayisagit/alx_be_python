# pattern_drawing.py

# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Draw the Pattern
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after completing a row
    row += 1