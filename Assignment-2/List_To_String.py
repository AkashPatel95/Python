#Write a Python program to convert a list of characters into a string.


def list_to_string(char_list):
    return ''.join(char_list)

char_list = ['H', 'e', 'l', 'l', 'o']
result_string = list_to_string(char_list)

print("List of characters:", char_list)
print("String:", result_string)
