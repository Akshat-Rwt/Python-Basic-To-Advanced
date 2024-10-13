marks = {
    "Akshat" : 100,
    "Shubham" : 56,
    "Rohan" : 23,
    0:"Harry"
}

# It gives up the output in the tuple form 
print(marks.items())

print(marks.keys()) # Show the Keys 
print(marks.values()) # Show the Values 

marks.update({"Akshat" : 99}) # Update the original dictionary 
print(marks)


# What is the difference between them
# Both give the same output but there is a difference between them 
print(marks.get("Akshat"))  # Output : 99
print(marks["Akshat"])      # Output : 99

#Suppose we change the value then look at the output 
print(marks.get("Akshat1"))  #Output :  None 
print(marks["Akshat1"])      #Output :  Error
