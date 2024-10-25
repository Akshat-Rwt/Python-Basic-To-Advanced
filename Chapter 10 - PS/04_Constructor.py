class Employee:
    
    language = "Py" # this is a class attribute
    salary = 120000

    def __init__(self , name , salary , language):  # dunder method which is automatically call
        self.name = name 
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


harry = Employee("Harry" , 130000 , "Javascript")
# harry.name = "Harry"
print(harry.name , harry.salary , harry.language)

# rohan = Employee()