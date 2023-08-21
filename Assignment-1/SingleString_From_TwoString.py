'''Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string. '''

# Get input strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Ensure both strings have at least 2 characters
if len(string1) >= 2 and len(string2) >= 2:
    # Swap the first two characters of each string
    swapped_string1 = string2[:2] + string1[2:]
    swapped_string2 = string1[:2] + string2[2:]
    
    # Combine the swapped strings with a space in between
    result = swapped_string1 + " " + swapped_string2
    print("Result:", result)
else:
    print("Both strings should have at least 2 characters.")
