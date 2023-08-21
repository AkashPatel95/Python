#Write a Python program to remove duplicates from a list.

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


original_list = [2, 3, 4, 2, 5, 6, 3, 7, 8, 5]
unique_elements = remove_duplicates(original_list)
print("Original List:", original_list)
print("List with Duplicates Removed:", unique_elements)
