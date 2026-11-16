
# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

# Define original variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# Test integer conversions
# a_int = int(a)  # ValueError: decimal string cannot convert directly to int
b_int = int(b)
# c_int = int(c)  # ValueError: string contains letters
# d_int = int(d)  # ValueError: string contains letters

# Test float conversions
a_float = float(a)
b_float = float(b)
# c_float = float(c)  # ValueError: string contains letters
# d_float = float(d)  # ValueError: string contains letters

# Convert a to float and then integer
a_int_from_float = int(float(a))

# Extract numeric portions using slicing
c_number = int(c[0:3])
d_number = int(d[7:8])

# Remove leading and trailing spaces
print(a.strip())
print(d.strip())

# Display original variables and their types
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# Display converted variables and their types
print(b_int, type(b_int))
print(a_float, type(a_float))
print(b_float, type(b_float))
print(a_int_from_float, type(a_int_from_float))
print(c_number, type(c_number))
print(d_number, type(d_number))

# Observations:
# int() works with b because it contains a whole number.
# int(a) produces a ValueError because a contains a decimal.
# float() works with a and b because both contain numeric text.
# c and d produce ValueErrors because they contain letters.
# int(float(a)) successfully converts a decimal string to an integer.
# Slicing extracts the numeric portions of c and d.
# strip() removes spaces at the beginning and end of a string.
