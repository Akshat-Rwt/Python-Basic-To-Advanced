# Write a program to print multiplication table of a given number using for loop.

number  = int ( input ("Enter the Number : "))

i = 1 
for i in range (1 , 11):
    print(number ,"X",i,"=",number*i)
    # print(f"{n} X {i} = {n*i}")