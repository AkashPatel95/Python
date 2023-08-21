#Write a Python function to check whether a number is in a given range.

def is_in_range(number, lower, upper):
    return lower <= number <= upper

lower_limit = 10
upper_limit = 20
num_to_check = 15

if is_in_range(num_to_check, lower_limit, upper_limit):
    print("{} is in the range [{}, {}]".format(num_to_check, lower_limit, upper_limit))
else:
    print("{} is not in the range [{}, {}]".format(num_to_check, lower_limit, upper_limit))

