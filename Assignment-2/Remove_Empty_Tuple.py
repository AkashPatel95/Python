#Write a Python program to remove an empty tuple(s) from a list of tuples.

# Create a list of tuples with empty tuples
tuples_list = [(1, 2), (), (3, 4), (), (5, 6), (), (), (7, 8)]

# Remove empty tuples from the list
filtered_list = []
for i in tuples_list:
    if i!=():
        filtered_list.append(i)

# Print the original list and the filtered list
print("Original list:", tuples_list)
print("Filtered list:", filtered_list)
