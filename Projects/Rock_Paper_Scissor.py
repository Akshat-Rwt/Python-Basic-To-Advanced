"""

WORKFLOW OF PROJECT
1- Input from the user(Rock , Paper , Scissor )
2- Computer Choice (Compiter will choose randomly not conditionally)
3- Result print

Cases: 
A - Rock
Rock - Rock = tie
Rock - Paper = Paper Win 
Rock - Scissor = Rock win

B - Paper
Paper - Paper = tie
Paper - Scissor = Scissor wins
Paper - Rock = Paper wins

C - Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock wins
Scissor - Paper = Scissor wins
"""

import random
item_list= ["Rock","Paper","Scissor"]

user_choice = input("Enter the user choice -  Rock , Paper , Scissor : ")
Computer_choice = random.choice(item_list)

print(f"User Choice = {user_choice} , Computer Choice = {Computer_choice}")

if user_choice == Computer_choice :
    print("Both choose same  = Match tie")

elif user_choice == "Rock":
    if Computer_choice == "Paper":
        print("Paper cover Rocks = Computer wins")
    else:
        print("Rock Smashes Scissor = User wins")


elif user_choice == "Paper":
    if Computer_choice == "Rock":
        print("Paper cover Rocks = user wins")
    else:
        print("Scissor Cuts Paper= Computer wins")


elif user_choice == "Scissor":
    if Computer_choice == "Paper":
        print("Scissor cuts Paper = User wins")
    else:
        print("Rock Smashes Scissor = Computer wins")