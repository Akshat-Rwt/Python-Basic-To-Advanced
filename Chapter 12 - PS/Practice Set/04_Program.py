# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.
try : 
    a = int(input("Enter the number : "))
    b = int(input("Enter the number : "))
    print(a/b)
    
except ZeroDivisionError as v : 

    print("Infinite")