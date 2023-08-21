#Write a python program to sum of the first n positive integers.

n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    sum_of_integers = 0
    for i in range(1, n + 1):
        sum_of_integers += i
    print("The sum of the first {} positive integers is {}.".format(n,sum_of_integers))
