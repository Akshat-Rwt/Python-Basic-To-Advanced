# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("Enter the Marks of Subject 1 : "))
sub2 = int(input("Enter the Marks of Subject 2 : "))
sub3 = int(input("Enter the Marks of Subject 3 : "))

avg = ((sub1 +  sub2 + sub3) * (100) ) / 300

if(avg >= 40 & sub1 >= 33 & sub2 >= 33 & sub3 >= 33 ):
    print("Pass, Promited ti next class") 

else:
    print("Failed")

