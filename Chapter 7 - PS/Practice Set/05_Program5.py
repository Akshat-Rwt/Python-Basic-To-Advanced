# Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter the Number : "))
i = 0 
sum = 0

while(i <= n):
    sum = sum + i
    i = i + 1

print("Sum of n natural number is : " , sum) 