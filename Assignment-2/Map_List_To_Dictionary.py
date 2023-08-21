#Write a Python program to map two lists into a dictionary.

# Two lists to map into a dictionary
keys = ['name', 'age', 'country']
values = ['Alice', 25, 'USA']

# Map lists into a dictionary
mapped_dict = dict(zip(keys, values))

# Print the original lists and the mapped dictionary
print("Keys list:", keys)
print("Values list:", values)
print("Mapped dictionary:", mapped_dict)
