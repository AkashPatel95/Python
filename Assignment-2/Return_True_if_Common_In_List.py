'''Write a Python function that takes two lists and returns true if they have 
at least one common member. '''

def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8, 9]

print("Do list_a and list_b have a common member?", has_common_member(list_a, list_b))
