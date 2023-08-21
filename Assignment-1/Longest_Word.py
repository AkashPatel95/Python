'''Write a Python function that takes a list of words and returns the length 
of the longest one.'''

def find_longest_word_length(word_list):
    longest_length = 0
    
    for word in word_list:
        if len(word) > longest_length:
            longest_length = len(word)
    
    return longest_length


words = ["apple", "banana", "cherry", "date", "elderberry"]
longest_length = find_longest_word_length(words)
print("The length of the longest word is:", longest_length)
