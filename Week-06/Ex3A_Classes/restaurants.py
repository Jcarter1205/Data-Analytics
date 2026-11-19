
# Exercise 3.A Working with Classes
# Lab 1: Restaurant Class

class Restaurant:
    '''A class that represents a restaurant and its type of food.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    # Display the restaurant name and type of food
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    # Display that the restaurant is open
    def rest_open(self):
        print(f"{self.rest_name} is open.")


# Create three restaurant instances
restaurant1 = Restaurant("Applebee's", "American food")
restaurant2 = Restaurant("Burger King", "fast food")
restaurant3 = Restaurant("Dunkin' Donuts", "coffee and donuts")


# Call the methods for each restaurant
restaurant1.describe_rest()
restaurant1.rest_open()

print()

restaurant2.describe_rest()
restaurant2.rest_open()

print()

restaurant3.describe_rest()
restaurant3.rest_open()
