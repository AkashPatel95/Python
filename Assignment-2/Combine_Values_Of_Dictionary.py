'''Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}] 
Expected Output:
Counter ({'item1': 1150, 'item2': 300})'''

from collections import Counter

# Sample data: List of dictionaries
data = [{'item': 'item1', 'amount': 400},
        {'item': 'item2', 'amount': 300},
        {'item': 'item1', 'amount': 750}]

# Combine values using Counter
combined_counter = Counter()

for d in data:
    combined_counter[d['item']] += d['amount']

# Print the original list of dictionaries and the combined Counter
print("Original data:", data)
print("Combined Counter:", combined_counter)
