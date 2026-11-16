
# Import the math module
import math

# Define the number of tourists
tourists = 38

# Define van capacity and rental price
van_capacity = 15
van_cost = 250

# Calculate the number of vans needed
vans_needed = math.ceil(tourists / van_capacity)

# Calculate the total rental cost
total_cost = vans_needed * van_cost

# Calculate the cost per person
cost_per_person = total_cost / tourists

# Display results
print(f"Number of tourists: {tourists}")
print(f"Number of vans needed: {vans_needed}")
print(f"Total van rental cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")
