import random

''' 
1 for snake
-1 for water
0 for gun

'''
computer = random.choice([1,-1,0])
youstr = input("enter your choice : ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = { 1 : "snake" , -1: "water" , 0 : "gun" }

you = youDict[youstr]


print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if (computer == you):
    print("its a draw")
    
elif((computer == -1 and you == 1) or
       (computer == 1 and you == 0) or
       (computer == 0 and you == -1)):
    print("You win!") 
else:
        print(" You lose!")    