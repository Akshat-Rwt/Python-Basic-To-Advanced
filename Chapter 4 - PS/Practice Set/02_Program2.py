# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

Student1 = int( input ("Enter the 1 Student Marks : ") )
marks.append(Student1)

Student2 = int( input ("Enter the 2 Student Marks : "))
marks.append(Student2)

Student3 = int ( input ("Enter the 3 Student Marks : "))
marks.append(Student3)

Student4 = int ( input ("Enter the 4 Student Marks : "))
marks.append(Student4)

Student5 = int ( input ("Enter the 5 Student Marks : "))
marks.append(Student5)

Student6 = int ( input ("Enter the 6 Student Marks : "))
marks.append(Student6)

print(marks)

marks.sort()
print(marks)

