'''Write a Python script to concatenate following dictionaries to create a 
new one.'''

# Define dictionaries to concatenate
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}

# Concatenate dictionaries to create a new one
concatenated_dict = {}

for d in [dict1, dict2, dict3]:
    concatenated_dict.update(d)

# Print the original dictionaries and the concatenated dictionary
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Dictionary 3:", dict3)
print("Concatenated dictionary:", concatenated_dict)
