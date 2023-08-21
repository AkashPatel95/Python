letter = input("Enter a letter: ")

if letter in ['a','e','i','o','u'] or letter in ['A','E','I','O','U']:
    print("{} is a vowel.".format(letter))
else:
    print("{} is a consonent.".format(letter))
