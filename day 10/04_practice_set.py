
# PROBLEM 1

# f = open("poem.txt")
# content = f.read()
# if("twinkle" in content):
#     print("twinkle is present in the poem.")
# else:
#     print("twinkleis not present in the poem.")   
# f.close()

# PROBLEM 2

# import random

# def game():
#     print("you are playing the game!")
#     score = random.randint(1, 50)
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if (hiscore !=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
            
#     print(f"your score: {score}") 
#     if(score>hiscore):
#         with open("hiscore.txt", "w") as f:
#                    f. write(str(score))
#     return score               
# game()

# PROBLEM 3

# def generateTable(n):
#     table = ""
#     for i in range(1, 11):
#         table +=f"{n} x {i} = {n*i}\n"
#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table)
        
# for i in range(2, 21):
#     generateTable(i)
            
# PROBLEM 4 

# word = "donkey"

# with open("file.txt", "r") as f:
#     content = f.read()
    
# newcontent = content.replace(word, "######")

# with open("file.txt", "w") as f:
#     f.write(newcontent)

# PROBLEM 5

# words = ["donkey", "stupid", "idiot"]

# with open("filee.txt", "r") as f:
#     content = f.read()

# for word in words:    
#      content = content.replace(word, "#" * len(word))

# with open("filee.txt", "w") as f:
#     f.write(content)

# PROBLEM 6

# with open("log.txt", "r") as f:
#     content = f.read()
    
# if("Python" in content):
#      print("Python is present in the log file.")
# else:
#     print("Python is not present in the log file.")

# PROBLEM 7

# with open("log.txt", "r") as f:
#     lines = f.readlines()
    
# lineno = 1
# for line in lines:
#     if("Python" in line):
#         print(f"Yes Python is present. Line no : {lineno}")    
#         break
#     lineno +=1
# else:
#     print("no, python is not present")    

# PROBLEM 8

# with open("this.txt") as f:
#     content = f.read()
    
# with open("this_copy.txt", "w") as f:
#     f.write(content)

# problem 9

# with open("this.txt")as f:
#     content1 = f.read()
    
# with open("this_copy.txt")as f:
#     content2 = f.read()
# if(content1 == content2):
#     print(" Yes, both files are identical")
# else:
#     print("No, the files are not identical")    

# PROBLEM 10

# with open("this.txt", "w") as f:
#     f.write("")

# problem 11

with open("old.txt") as f:
    content = f.read()
    
    with open("renamed_by_pyton.txt", "w") as f:
        f.write(content)