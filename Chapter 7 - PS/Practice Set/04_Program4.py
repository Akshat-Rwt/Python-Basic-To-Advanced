# Write a program to find whether a given number is prime or not.

n = int(input("Enter the Number : "))

prime = True 
for i in range (2 , int(n/2)):
    if(n % i == 0):
        prime = False
        break
    else:
        prime = True
        break

if(prime == False):
    print("PRIME NUMBER") 

else:
    print("NOT PRIME NUMBER")
