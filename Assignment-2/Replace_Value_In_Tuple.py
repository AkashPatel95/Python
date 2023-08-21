#Write a Python program to replace last value of tuples in a list.

# Create a list of tuples
tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# Value to replace the last element with
new_last_value = 10

# Create an empty list to store the modified tuples
modified_list = []

# Iterate through each tuple in the list
for t in tuples_list:
    # Create a new tuple with the last value replaced
    modified_tuple = (*t[:-1], new_last_value)
    
    # Append the modified tuple to the new list
    modified_list.append(modified_tuple)

# Print the original list and the modified list
print("Original list:", tuples_list)
print("Modified list:", modified_list)
