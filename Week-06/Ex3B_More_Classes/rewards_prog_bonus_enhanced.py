
# Exercise 3.B More Fun with Classes
# Lab 2: Enhanced Rewards Program

class RewardsProgram:
    '''A class that tracks a customer's restaurant visits and rewards points.'''

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []
        self.rewards_points = {}

    # Display the customer's profile
    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    # Thank the customer
    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    # Calculate rewards points for a restaurant visit
    def calculate_rewards(self, restaurant, food_bill):
        points = int(food_bill)

        if restaurant not in self.rewards_points:
            self.rewards_points[restaurant] = 0

        self.rewards_points[restaurant] += points

        return points

    # Record a restaurant visit and calculate points
    def visit_rest(self):
        restaurant = input("Name of restaurant: ")

        if restaurant not in self.restaurants_visited:
            self.restaurants_visited.append(restaurant)

        while True:
            try:
                food_bill = float(
                    input("What was the total food bill for this visit? ")
                )

                if food_bill < 0:
                    print("Please enter a positive bill amount.")
                else:
                    break

            except ValueError:
                print("Please enter a valid dollar amount.")

        points = self.calculate_rewards(restaurant, food_bill)

        total_points = sum(self.rewards_points.values())

        print(f"Points for this visit: {points}")
        print(f"Total rewards points earned: {total_points}")
        print(f"Thank you for visiting {restaurant}!")


# Create a customer instance
customer1 = RewardsProgram(
    "Jada Carter",
    "215-555-0123",
    "jada@example.com"
)

# Display the customer's profile
customer1.profile()
print()

# Record several restaurant visits
customer1.visit_rest()
print()

customer1.visit_rest()
print()

customer1.visit_rest()

# Display the restaurants visited
print("\nRestaurants Visited:")
print(customer1.restaurants_visited)

# Display the rewards balance for each restaurant
print("\nRewards Points by Restaurant:")
print(customer1.rewards_points)
