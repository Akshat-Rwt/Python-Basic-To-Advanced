# Write a program using functions to find greatest of three numbers.

def greater(a,b,c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c
    
n = greater(10,340,30)
print(n)