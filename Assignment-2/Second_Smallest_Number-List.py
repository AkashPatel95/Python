#Write a Python program to find the second smallest number in a list. 


numbers_list = [5, 2, 8, 1, 3, 7]

unique_number=list(set(numbers_list))

sorted_unique_number=sorted(unique_number)

print("Second Smallest Number:",sorted_unique_number[1])
