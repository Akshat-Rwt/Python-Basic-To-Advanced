# Write a program to find the greatest of four numbers entered by the user.

num1 = int(input("Enter the Number : "))
num2 = int(input("Enter the Number : "))
num3 = int(input("Enter the Number : "))
num4 = int(input("Enter the Number : "))

if((num1 > num2) & (num1 > num3) & (num1 > num4)):
    print("num1 is the greatest number : " , num1)

elif((num2 > num1) & (num2 > num3) & (num2 > num4)):
    print("num2 is the greatest number : " , num2)

elif((num3 > num2) & (num3 > num1) & (num3 > num4)):
    print("num3 is the greatest number : " , num3)

elif((num4 > num2) & (num4 > num3) & (num4 > num1)):
    print("num4 is the greatest number : " , num4)

else:
    print("Error")