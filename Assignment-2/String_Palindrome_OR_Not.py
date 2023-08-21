'''Write a Python function that checks whether a passed string is 
palindrome or not'''

def palindrome(string):
    reversed_string = string[::-1]
    if reversed_string == string:
        print("String is a palindrome.")
    else:
        print("String is not a palindrome.")

str1 = input("Enter a string: ")
palindrome(str1)
