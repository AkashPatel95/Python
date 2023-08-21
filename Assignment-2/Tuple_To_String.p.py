#Write a Python program to convert a tuple to a string.


# Create a tuple with numbers
numbers_tuple = (1, 2, 3, 4, 5)

# Convert the tuple to a string
numbers_string = ', '.join(map(str, numbers_tuple))

# Print the converted string
print(numbers_string)
