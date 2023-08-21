#Write a Python program to returns sum of all divisors of a number.

def sum_of_divisors(number):
    divisors_sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum


num = int(input("Enter a number: "))
result = sum_of_divisors(num)
print("Sum of divisors of {} is: {}".format(num, result))
