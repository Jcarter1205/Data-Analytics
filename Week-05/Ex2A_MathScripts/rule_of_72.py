
# Define current savings and interest rate
current_savings = 1000.00
interest_rate = 6

# Calculate the time needed to double savings
years = 72 / interest_rate

# Calculate the doubled savings balance
doubled_balance = current_savings * 2

# Display results
print("Your current savings is " + format(current_savings, ".2f") + ".")
print("At a " + format(interest_rate / 100, ".0%") + " interest rate, your savings account will be")
print("worth " + format(doubled_balance, ".2f") + " in " + format(years, ".1f") + " years")
