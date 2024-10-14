#Write a program to calculate the grade of a student from his marks from the following scheme:
#90 – 100 => Ex
#80 – 90 => A
#70 – 80 => B
#60 – 70 =>C
#50 – 60 => D
#<50 => F

Name  = input("Enter the name : ")
Marks = int(input("Enter the marks : "))

if(Marks > 90 & Marks < 100):
    print("Excellent")

elif(Marks > 80 & Marks < 90):
    print("A")

elif(Marks > 70 & Marks < 80):
    print("B")

elif(Marks > 60 & Marks < 70):
    print("C")

elif(Marks > 50 & Marks < 60):
    print("D")

elif( Marks < 50):
    print("F")

else:
    print("Fail")