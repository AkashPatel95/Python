'''Write a Python program to count the number of characters (character 
frequency) in a string '''

from collections import Counter

string = input("Enter a string: ")

# Use Counter to count character frequencies
char_frequency = Counter(string)

# Print character frequencies using the .format() method
print("Character frequencies:")
for char, frequency in char_frequency.items():
    print("'{}': {}".format(char, frequency))
