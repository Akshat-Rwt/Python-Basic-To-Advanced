a = int(input("Enter the number : "))
b = int(input("Enter the number : "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide number by zero ")

else:
    print(f" The deivision of a/b is : {a/b}")