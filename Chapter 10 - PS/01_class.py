class Employee:
    
    language = "Py" # this is a class attribute
    salary = 120000

harry = Employee()
harry.name = "Harry" # this is an object attribute / Instance attribute 
print(harry.name , harry.salary , harry.language)

rohan = Employee()
rohan.name = "rohan"
print(rohan.name , rohan.salary , rohan.language)

# Here name is object attribute and salary and language are class attribute as they directly belong to the class 