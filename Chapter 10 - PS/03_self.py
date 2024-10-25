class Employee:
    
    language = "Py" # this is a class attribute
    salary = 120000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee()
harry.language = "Javascript" # this is an object attribute / Instance attribute 
print(harry.salary , harry.language)

# harry.getinfo()
Employee.getinfo(harry)

