 """
This script processes a list of integers to create a tuple of unique integers.
It also determines and displays the minimum and maximum numbers from the tuple.
"""

integers = [5, 3, 2, 5, 7, 3, 9, 2]

# Create a tuple of unique integers
unique_integers = tuple(set(integers))

# Find the minimum and maximum numbers
min_number = min(unique_integers)
max_number = max(unique_integers)

# Display results
print(f"Tuple of unique integers: {unique_integers}")
print(f"Minimum number: {min_number}")
print(f"Maximum number: {max_number}")
