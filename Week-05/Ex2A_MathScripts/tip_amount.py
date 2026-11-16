
# Define the restaurant bill and tip percentage
restaurant_bill = 60.00
tip_percentage = 20

# Calculate the tip amount
tip_amount = restaurant_bill * (tip_percentage / 100)

# Display the result
print("The tip on a $" + str(restaurant_bill) + " restaurant bill is $" + format(tip_amount, ".2f"))
