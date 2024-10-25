class Employee:
    
    language = "Py" # this is a class attribute
    salary = 120000

harry = Employee()
harry.language = "Javascript" # this is an object attribute / Instance attribute 
print(harry.salary , harry.language)

rohan = Employee()
rohan.name = "rohan"
print(rohan.name , rohan.salary , rohan.language)
