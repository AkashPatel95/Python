#Write a Python program to print all unique values in a dictionary.

# Sample dictionary
my_dict = {'a': 100, 'b': 200, 'c': 100, 'd': 300, 'e': 200}

# Get unique values using set
unique_values = set(my_dict.values())

# Print the original dictionary and the unique values
print("Original dictionary:", my_dict)
print("Unique values:", unique_values)
