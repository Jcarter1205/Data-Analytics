
# Define original names
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

# Define original salaries
salary_1 = "$82,500"
salary_2 = "$74,000"

# Convert names to lowercase
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# Convert names to title case
print(name_1.title())
print(name_2.title())
print(name_3.title())

# Remove dollar signs from salaries
clean_salary_1 = salary_1.replace("$", "")
clean_salary_2 = salary_2.replace("$", "")

# Display cleaned salaries
print(clean_salary_1)
print(clean_salary_2)

# Check the data types
print(type(clean_salary_1))
print(type(clean_salary_2))

# Convert salary strings into usable integers
usable_salary_1 = int(salary_1.replace("$", "").replace(",", ""))
usable_salary_2 = int(salary_2.replace("$", "").replace(",", ""))

# Display integer salaries and their types
print(usable_salary_1)
print(type(usable_salary_1))
print(usable_salary_2)
print(type(usable_salary_2))
