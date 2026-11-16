
# Ask the user for the rectangle dimensions
side_a = float(input("What is the length of the first side? "))
side_b = float(input("What is the length of the second side? "))

# Calculate the area
area = side_a * side_b

# Display results
print("Side A is " + str(side_a))
print("Side B is " + str(side_b))
print("The area of the rectangle is " + str(area))

# Observation:
# input() initially collects information as text.
# float() converts the input into a number so Python can perform calculations.
# If the user enters letters instead of numbers, the calculation will produce an error.
