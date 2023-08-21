'''Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings. '''


def count_strings_with_same_first_last(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count


string_list = ["abca", "hello", "wow", "python", "pop"]
result = count_strings_with_same_first_last(string_list)
print("Number of strings with same first and last character:", result)
