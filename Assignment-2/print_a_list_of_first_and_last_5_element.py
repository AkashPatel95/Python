'''Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30. '''

def generate_square_list(start, end):
    square_list = [num ** 2 for num in range(start, end + 1)]
    return square_list

# Generate the list of squares for numbers between 1 and 30
squared_numbers = generate_square_list(1, 30)

# Print the first 5 elements
print("First 5 elements:", squared_numbers[:5])

# Print the last 5 elements
print("Last 5 elements:", squared_numbers[-5:])
