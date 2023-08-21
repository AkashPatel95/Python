#Write a Python program to find the highest 3 values in a dictionary .

# Sample dictionary
my_dict = {'a': 100, 'b': 300, 'c': 200, 'd': 500, 'e': 400}

# Get the highest 3 values from the dictionary
highest_values = sorted(my_dict.values(), reverse=True)

# Print the original dictionary and the highest 3 values
print("Original dictionary:", my_dict)
print("Highest 3 values:", highest_values[:3])
