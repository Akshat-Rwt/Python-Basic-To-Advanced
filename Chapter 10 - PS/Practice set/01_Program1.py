# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer():
    company = "Microsoft"
    def __init__(self,name , salary, pincode):
        self.name= name
        self.salary = salary
        self.pincode = pincode

p = Programmer("Harry" , 1200000 , 248407)
print(p.name, p.salary,p.pincode)
        