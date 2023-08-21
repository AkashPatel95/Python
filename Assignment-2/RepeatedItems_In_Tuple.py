#Write a Python program to find the repeated items of a tuple.

# Create a tuple with elements
my_tuple = (1, 2, 2, 3, 4, 4, 5, 5)

# Find repeated items in the tuple
repeated_items = []
seen_items = set()

for item in my_tuple:
    if item in seen_items:
        repeated_items.append(item)
    else:
        seen_items.add(item)

# Convert the list of repeated items to a set to remove duplicates
repeated_items_set = set(repeated_items)

# Print the repeated items
print("Repeated items:", repeated_items_set)
