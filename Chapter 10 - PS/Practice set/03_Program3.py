# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
# Solution : - No Class Attribute is not Changed 
class Demo:
    a = 4

o = Demo()
print(o.a) # Print class attribute because instance attribute is not present
o.a = 0     # Instance attribute is present 
print(o.a) # Print instance attribute 
print(Demo.o)

