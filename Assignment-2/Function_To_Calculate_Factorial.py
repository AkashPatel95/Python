'''Write a Python function to calculate the factorial of a number (a 
nonnegative integer)'''

def factorial(num):
    factorial=1
    for i in range(1,num+1):
        factorial*=i
    print("factorial is:",factorial)


number=int(input("enter a number:"))
factorial(number)
