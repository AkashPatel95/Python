'''Write a Python program to find the first appearance of the substring 
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
whole 'not'...'poor' substring with 'good'. Return the resulting string'''

# Get input string from the user
input_string = input("Enter a string: ")

# Find the indices of 'not' and 'poor' substrings
index_not = input_string.find('not')
index_poor = input_string.find('poor')

# Check if both substrings are found and 'poor' comes after 'not'
if index_not>0 and index_poor>0 and index_poor > index_not:
    input_string=input_string.replace(input_string[index_not:(index_poor+4)],'good')
    print("Result:", input_string)
else:
   print("Result:", input_string)


