upper_limit = int(input("Enter the upper limit: "))

a, b = 0, 1

print("Fibonacci series:")
print(a, end=" ")

for i in range(1, upper_limit + 1):
    if b <= upper_limit:
        print(b, end=" ")
        a, b = b, a + b
    
