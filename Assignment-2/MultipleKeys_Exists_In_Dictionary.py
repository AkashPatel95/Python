#Write a Python program to check multiple keys exists in a dictionary .

# Sample dictionary
my_dict = {'apple': 3, 'banana': 5, 'orange': 2, 'grapes': 7, 'kiwi': 1}

# Keys to check
keys_to_check = ['apple', 'banana', 'watermelon']

# Check if the keys exist in the dictionary
for key in keys_to_check:
    if key in my_dict:
        print("The key '{}' exists in the dictionary.".format(key))
    else:
        print("The key '{}' does not exist in the dictionary.".format(key))
