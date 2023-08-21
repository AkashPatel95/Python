#Write a Python program to create a dictionary from a string.

# Sample string
sample_string = "apple=3, banana=5, orange=2, grapes=7, kiwi=1"

# Split the string by comma and space to separate key-value pairs
key_value_pairs = sample_string.split(", ")

# Create a dictionary from the key-value pairs
result_dict = {}

for pair in key_value_pairs:
    key, value = pair.split("=")
    result_dict[key] = int(value)

# Print the original string and the created dictionary
print("Original string:", sample_string)
print("Created dictionary:", result_dict)
