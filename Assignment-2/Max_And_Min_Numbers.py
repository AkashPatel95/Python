'''Write a Python program to find the maximum and minimum numbers 
from the specified decimal numbers.'''
def find_max_min(numbers):
    if not numbers:
        return None, None  # Return None if the list is empty

    max_number = max(numbers)
    min_number = min(numbers)
    return max_number, min_number


decimal_numbers = [5.4, 8.2, 3.7, 9.1, 2.6]

max_num, min_num = find_max_min(decimal_numbers)
print("Maximum number: {:.2f}".format(max_num))
print("Minimum number: {:.2f}".format(min_num))
