
# Exercise 4.A - Practicing Read/Write
# Lab 1

# Step 10: Open the file in read mode
f = open("about_me.txt", "r")

# Step 11: Read and print the contents of the file
print("Step 11: Read the entire file")
print(f.read())

f.close()


# Step 12: Read 50 characters at a time
f = open("about_me.txt", "r")

print("\nStep 12: Read 50 characters")
print(f.read(50))
print(f.read(50))

f.close()


# Step 13: Experiment with readline()
f = open("about_me.txt", "r")

print("\nStep 13: Read lines")
print(f.readline(10))
print(f.readline())

for i in range(1, 5):
    print(f.readline())

f.close()


# Step 14: Experiment with readlines()
f = open("about_me.txt", "r")

print("\nStep 14: Read lines into a list")
print(f.readlines(1))
print(f.readlines(1))
print(f.readlines(10))
print(f.readlines(10))

f.close()


# Step 15: Combine different reading methods
f = open("about_me.txt", "r")

# Read the first 50 characters
first_variable = f.read(50)

# Create an empty list for the next four lines
second_variable = []

# Read the next four lines
for i in range(1, 5):
    second_variable.append(f.readline())

# Read the next 100 characters as complete lines
third_variable = f.readlines(100)

f.close()


# Step 16: Print the results
print("\nStep 16: Combined reading methods")

print("First 50 characters:", first_variable)

print("Next four lines, as list by line:", second_variable)

print("Next 100 characters, as list by line, rounded up to complete lines:", third_variable)
