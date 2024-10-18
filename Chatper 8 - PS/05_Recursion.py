'''
Factorial(1) = 1 
Factorial(2) = 2 X 1 
Factorial(3) = 3 X 2 X 1 
Factorial(4) = 4 X 3 X 2 X 1 
Factorial(5) = 5 X 4 X 3 X 2 X 1 

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1) 

n = int(input("Enter the number : "))
n = factorial(5)
print(f"Factorial of the number is : {n}")