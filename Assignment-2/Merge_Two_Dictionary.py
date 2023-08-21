#Write a Python script to merge two Python dictionaries.

# Two dictionaries to merge
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dictionaries using dictionary methods
merged_dict = dict1.copy()
merged_dict.update(dict2)

# Print the original dictionaries and the merged dictionary
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged dictionary:", merged_dict)
