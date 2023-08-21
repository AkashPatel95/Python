# Swapping with a temporary variable
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Before swapping: num1 = {}, num2 = {}".format(num1, num2))

temp = num1
num1 = num2
num2 = temp

print("After swapping with temp variable: num1 = {}, num2 = {}".format(num1, num2))

# Swapping without a temporary variable
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Before swapping: num1 = {}, num2 = {}".format(num1, num2))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping without temp variable: num1 = {}, num2 = {}".format(num1, num2))
