'''Write a Python script to check if a given key already exists in a 
dictionary.'''

# Sample dictionary
my_dict = {'apple': 3, 'banana': 5, 'orange': 2, 'grapes': 7, 'kiwi': 1}

# Key to check
key_to_check = 'banana'

# Check if the key exists in the dictionary
if key_to_check in my_dict:
    print("The key '{}' exists in the dictionary.".format(key_to_check))
else:
    print("The key '{}' does not exist in the dictionary.".format(key_to_check))
