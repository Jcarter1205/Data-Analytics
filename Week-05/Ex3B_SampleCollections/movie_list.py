
# Create a list of favorite movies
movie_list = [
    "The Notebook",
    "Black Panther",
    "Mean Girls",
    "Inception",
    "Titanic"
]

# Display the list description
print(f"The list movie_list includes my top {len(movie_list)} favorite movies")

# Display the complete list
print(movie_list)

# Display a sorted version of the list
print(sorted(movie_list))

# Display the original list again
print(movie_list)

# Sort the original list permanently
movie_list.sort()

# Display the updated list
print(movie_list)

# Add another movie
movie_list.append("Avatar")

# Display updated description
print(f"The list movie_list now includes {len(movie_list)} favorite movies")

# Display updated list
print(movie_list)

# Observations:
# sorted() displays a sorted copy without changing the original list.
# sort() permanently changes the original list.
# append() adds a new item to the end of the list.
