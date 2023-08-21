'''Write a Python script to sort (ascending and descending) a dictionary by 
value.'''


# Sample dictionary
my_dict = {'apple': 3, 'banana': 5, 'orange': 2, 'grapes': 7, 'kiwi': 1}

# Sort the dictionary by value in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sort the dictionary by value in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# Print the original dictionary and the sorted dictionaries
print("Original dictionary:", my_dict)
print("Sorted dictionary (ascending):", sorted_dict_asc)
print("Sorted dictionary (descending):", sorted_dict_desc)
