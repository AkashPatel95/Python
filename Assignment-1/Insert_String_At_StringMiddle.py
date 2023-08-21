#Write a Python function to insert a string in the middle of a string.


def insert_string_in_middle(original_string, insert_string, position):
   
    result = original_string[:position] + insert_string + original_string[position:]
    return result


original = "Hello, world!"
to_insert = "awesome "
position_to_insert = len(original) // 2
new_string = insert_string_in_middle(original, to_insert, position_to_insert)
print("Result:", new_string)
