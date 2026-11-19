
# Exercise 3.B More Fun with Classes
# Lab 1: Enhanced Restaurant Class

class Restaurant:
    '''A class that represents a restaurant and tracks customer activity and ratings.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    # Describe the restaurant
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    # Display restaurant status
    def rest_open(self):
        print(f"{self.rest_name} is open.")

    # Add the number of customers served
    def add_num_served(self):
        while True:
            try:
                customers = int(input("How many customers served today? "))

                if customers < 0:
                    print("Please enter a positive whole number.")
                else:
                    self.number_served += customers
                    break

            except ValueError:
                print("Please enter a whole number.")

    # Display the total number of customers served
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    # Collect and calculate customer ratings
    def customer_rating(self):
        while True:
            try:
                rating = int(input(
                    "How would you rate your experience today on a scale of 1-5 (5 being excellent)? "
                ))

                if 1 <= rating <= 5:
                    self.customer_ratings.append(rating)
                    average = sum(self.customer_ratings) / len(self.customer_ratings)

                    print(f"Your rating was {rating}. "
                          f"The average rating for this restaurant is {average:.2f}.")
                    break
                else:
                    print("Invalid rating. Please enter an integer from 1 to 5.")

            except ValueError:
                print("Invalid input. Please enter a whole number from 1 to 5.")


# Create three restaurant instances
restaurant1 = Restaurant("Applebee's", "American food")
restaurant2 = Restaurant("Burger King", "fast food")
restaurant3 = Restaurant("Dunkin' Donuts", "coffee and donuts")


# Test Applebee's
print("\n--- Applebee's ---")
restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()

restaurant1.customer_rating()
restaurant1.customer_rating()
restaurant1.customer_rating()


# Test Burger King
print("\n--- Burger King ---")
restaurant2.print_num_served()
restaurant2.add_num_served()
restaurant2.add_num_served()
restaurant2.print_num_served()

restaurant2.customer_rating()
restaurant2.customer_rating()
restaurant2.customer_rating()


# Test Dunkin' Donuts
print("\n--- Dunkin' Donuts ---")
restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served()

restaurant3.customer_rating()
restaurant3.customer_rating()
restaurant3.customer_rating()
