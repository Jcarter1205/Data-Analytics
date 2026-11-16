
# Import the math module
import math

# Define the room dimensions
length = 15
width = 12

# Define the number of tiles per box
tiles_per_box = 12

# Define the extra tile percentage
extra_percentage = 0.10

# Calculate the room area
room_area = length * width

# Calculate the number of tiles needed with 10% extra
tiles_needed = room_area * (1 + extra_percentage)

# Calculate the number of boxes to purchase
boxes_needed = math.ceil(tiles_needed / tiles_per_box)

# Display results
print(f"Room area: {room_area} square feet")
print(f"Tiles needed with 10% extra: {tiles_needed}")
print(f"Total boxes to purchase: {boxes_needed}")
