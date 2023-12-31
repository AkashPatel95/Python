'''Write a Python program to combine two dictionary adding values for 
common keys. 
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} 
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).'''

from collections import Counter

# Two dictionaries to combine
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine dictionaries by adding values for common keys
combined_dict = Counter(d1) + Counter(d2)

# Print the original dictionaries and the combined dictionary
print("Dictionary 1:", d1)
print("Dictionary 2:", d2)
print("Combined dictionary:", combined_dict)
