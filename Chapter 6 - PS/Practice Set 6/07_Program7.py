# Write a program to find out whether a given post is talking about “Harry” or not.

l = "Harry"

post = input("Write a post : ")

if(l.lower() in post.lower()) :
    print("Yes, This post is about the Harry")

else:
    print("No, This post is not about the Harry")