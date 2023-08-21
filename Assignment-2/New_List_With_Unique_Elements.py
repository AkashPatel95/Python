'''Write a Python function that takes a list and returns a new list with unique 
elements of the first list. '''

def get_unique_elements(input_list):
    unique_list = list(set(input_list))
    return unique_list

original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_elements = get_unique_elements(original_list)

print("Original List:", original_list)
print("List with Unique Elements:", unique_elements)
