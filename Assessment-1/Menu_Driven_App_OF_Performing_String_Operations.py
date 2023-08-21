#Menu driven application that can perform all string operations.

def reverse_string(input_str):
    return input_str[::-1]

def concatenate_strings(str1, str2):
    return str1 + str2

def is_palindrome(input_str):
    return input_str == input_str[::-1]

def copy_string(input_str):
    return input_str

def count_characters(input_str, char):
    return input_str.count(char)

def count_vowels_and_consonants(input_str):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

    vowel_count = sum(1 for char in input_str if char in vowels)
    consonant_count = sum(1 for char in input_str if char in consonants)

    return vowel_count, consonant_count

def count_spaces_and_digits(input_str):
    space_count = input_str.count(" ")
    digit_count = sum(1 for char in input_str if char.isdigit())

    return space_count, digit_count

while True:
    print("\nString Operations Menu:")
    print("1. Reverse a string")
    print("2. Concatenate strings")
    print("3. Check palindrome")
    print("4. Copy a string")
    print("5. Length of the string")
    print("6. Frequency of character in a string")
    print("7. Find number of vowels and consonants")
    print("8. Find number of blank spaces and digits")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        input_str = input("Enter a string: ")
        reversed_str = reverse_string(input_str)
        print("Reversed string:", reversed_str)
    elif choice == "2":
        str1 = input("Enter the first string: ")
        str2 = input("Enter the second string: ")
        concatenated_str = concatenate_strings(str1, str2)
        print("Concatenated string:", concatenated_str)
    elif choice == "3":
        input_str = input("Enter a string: ")
        if is_palindrome(input_str):
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")
    elif choice == "4":
        input_str = input("Enter a string: ")
        copied_str = copy_string(input_str)
        print("Copied string:", copied_str)
    elif choice == "5":
        input_str = input("Enter a string: ")
        length = len(input_str)
        print("Length of the string:", length)
    elif choice == "6":
        input_str = input("Enter a string: ")
        char = input("Enter the character to count: ")
        char_count = count_characters(input_str, char)
        print(f"Frequency of '{char}' in the string:", char_count)
    elif choice == "7":
        input_str = input("Enter a string: ")
        vowel_count, consonant_count = count_vowels_and_consonants(input_str)
        print("Number of vowels:", vowel_count)
        print("Number of consonants:", consonant_count)
    elif choice == "8":
        input_str = input("Enter a string: ")
        space_count, digit_count = count_spaces_and_digits(input_str)
        print("Number of blank spaces:", space_count)
        print("Number of digits:", digit_count)
    elif choice == "9":
        print("Thank you for using our application.Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

