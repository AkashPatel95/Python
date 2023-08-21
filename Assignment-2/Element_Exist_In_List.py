'''Write a Python program to check whether an element exists within a 
tuple. '''

# Create a tuple with some elements
my_tuple = (10, 20, 30, 40, 50)

# Element to check
element_to_check = 30

# Check if the element exists in the tuple
if element_to_check in my_tuple:
    print("{} exists in the tuple.".format(element_to_check))
else:
    print("{} does not exist in the tuple.".format(element_to_check))
