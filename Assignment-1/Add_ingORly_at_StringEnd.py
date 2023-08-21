'''Write a Python program to add 'ing' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then add 
'ly' instead if the string length of the given string is less than 3, leave it 
unchanged. '''

# Get input string from the user
input_string = input("Enter a string: ")

# Check if the string length is at least 3
if len(input_string) >= 3:
    # Check if the string already ends with 'ing'
    if input_string.endswith('ing'):
        result = input_string + 'ly'
    else:
        result = input_string + 'ing'
else:
    result = input_string

print("Result:", result)
