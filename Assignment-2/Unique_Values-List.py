#Write a Python program to get unique values from a list.

def get_unique_values(input_list):
    unique_values = list(set(input_list))
    return unique_values

original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_values = get_unique_values(original_list)

print("Original List:", original_list)
print("Unique Values:", unique_values)
