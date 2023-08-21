#How Do You Traverse Through A Dictionary Object In Python?

my_dict = {"apple": 3, "banana": 5, "orange": 2}

# Using a for loop to iterate through keys
print("Keys:")
for key in my_dict:
    print(key)

# Using a for loop to iterate through values
print("\nValues:")
for value in my_dict.values():
    print(value)

# Using a for loop to iterate through key-value pairs
print("\nKey-Value Pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
