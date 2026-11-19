
# Exercise 3.A Working with Classes
# Lab 2: Rewards Program Bonus

# Create a global list to store customer information
cust_list = []


class RewardsProgram:
    '''A class that stores customer information for a restaurant rewards program.'''

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    # Display the customer's profile
    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    # Thank the customer for visiting
    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    # Add customer information to the global customer list
    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))


# Create three customer instances
customer1 = RewardsProgram("Jada Carter", "215-555-0123", "jada@gmail.com")
customer2 = RewardsProgram("Anna Smith", "215-555-0456", "anna@gmail.com")
customer3 = RewardsProgram("Michael Brown", "215-555-0789", "michael@gmail.com")


# Display information and add each customer to the list
customer1.profile()
customer1.thank_you()
customer1.add_to_cust_list()

print()

customer2.profile()
customer2.thank_you()
customer2.add_to_cust_list()

print()

customer3.profile()
customer3.thank_you()
customer3.add_to_cust_list()


# Display the final customer list
print("\nCustomer List:")
print(cust_list)
