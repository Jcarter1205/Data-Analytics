
# Create a tuple of candy types
candy_types = ("Gummies", "Lollipops", "Hard Candy")

# Create a tuple of fruity flavors
fruit_flavors = ("Strawberry", "Mango", "Watermelon")

# Create a set of candy combinations
candy_combinations = {
    candy_types[0] + " - " + fruit_flavors[1],
    candy_types[1] + " - " + fruit_flavors[0],
    candy_types[2] + " - " + fruit_flavors[2]
}

# Display candy options
print("Today's candy options include:")
print(candy_combinations)
