'''Write a Python script to print a dictionary where the keys are numbers 
between 1 and 15.'''

# Create an empty dictionary
my_dict = {}

# Fill the dictionary with keys between 1 and 15 and their squares
for i in range(1, 16):
    my_dict[i] = i ** 2

# Print the dictionary
print("Dictionary with keys between 1 and 15:")
print(my_dict)
