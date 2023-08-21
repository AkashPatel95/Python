num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 == num2 or num2 == num3 or num1 == num3:
    print("Sum is 0")
else:
    sum_of_numbers = num1 + num2 + num3
    print("Sum:", sum_of_numbers)
