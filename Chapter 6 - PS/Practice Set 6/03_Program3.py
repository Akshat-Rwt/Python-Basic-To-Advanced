# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this”"  
p4 = "click this"

Message  =  input("Enter the comments : ")

if((p1 in Message) or (p2 in Message) or (p3 in Message) or (p4 in Message)):
    print("SPAM")

else:
    print("NOT SPAM")