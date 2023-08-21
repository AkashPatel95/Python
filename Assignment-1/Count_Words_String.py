'''Write a Python program to count the occurrences of each word in a 
given sentence .
'''

sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split(" ")

# Initialize an empty dictionary to store word frequencies
word_frequency = {}

# Count the occurrences of each word using the count() method
for word in words:
    count = words.count(word)
    word_frequency[word] = count

# Print word frequencies
print("Word frequencies:")
for word, frequency in word_frequency.items():
    print("'{}': {}".format(word, frequency))
