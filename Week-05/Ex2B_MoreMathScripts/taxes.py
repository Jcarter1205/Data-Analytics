
# Define monthly salary
monthly_salary = 4000.00

# Define federal tax rate
tax_rate = 0.23

# Calculate taxes withheld
taxes_withheld = monthly_salary * tax_rate

# Calculate remaining salary after taxes
remaining_salary = monthly_salary - taxes_withheld

# Display results
print(f"Monthly salary: ${monthly_salary:.2f}")
print(f"Federal taxes withheld: ${taxes_withheld:.2f}")
print(f"Salary after taxes: ${remaining_salary:.2f}")
