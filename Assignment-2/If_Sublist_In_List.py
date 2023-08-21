'''Write a Python program to check whether a list contains a sub list'''

def contains_sublist(main_list, sub_list):
    if len(sub_list) == 0:
        return True
    
    for i in range(len(main_list) - len(sub_list) + 1):
        if main_list[i:i + len(sub_list)] == sub_list:
            return True
    
    else:
        return False


main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list1 = [3, 4, 5]
sub_list2 = [6, 7, 8, 10]

print("Does main_list contain sub_list1?", contains_sublist(main_list, sub_list1))
print("Does main_list contain sub_list2?", contains_sublist(main_list, sub_list2))
