''' Write a Python function to get the largest number, smallest num and sum 
of all from a list. '''

def analyze_list(numbers):
    
    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)

    return largest, smallest, total_sum


numbers_list = [2, 33, 222, 14, 25]
largest_num, smallest_num, sum_of_all = analyze_list(numbers_list)

print("Largest number:", largest_num)
print("Smallest number:", smallest_num)
print("Sum of all numbers:", sum_of_all)
