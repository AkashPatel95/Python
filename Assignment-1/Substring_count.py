#Write a Python program to count occurrences of a substring in a string.

string = input("Enter a string: ")
substring = input("Enter a substring to count: ")

count = string.count(substring)
print("The substring '{}' appears {} times in the string.".format(substring, count))
