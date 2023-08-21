#Write a Python program to split a list into different variables.


def split_list_to_variables(input_list):
    if len(input_list) >= 3:
        first, *middle, last = input_list
        return first, middle, last
    else:
        return None


input_list = [1, 2, 3, 4, 5]
result = split_list_to_variables(input_list)

if result:
    first_item, middle_items, last_item = result
    print("First item:", first_item)
    print("Middle items:", middle_items)
    print("Last item:", last_item)
else:
    print("The input list should have at least three elements.")
