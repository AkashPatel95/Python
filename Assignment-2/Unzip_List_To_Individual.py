#Write a Python program to unzip a list of tuples into individual lists.

# Create a list of tuples
tuples_list = [(1, 4), (2, 5), (3, 6)]

# Unzip the list of tuples into individual lists
unzipped_lists = list(zip(*tuples_list))

# Print the original list of tuples and the unzipped lists
print("Original list of tuples:", tuples_list)
print("Unzipped lists:", unzipped_lists)
