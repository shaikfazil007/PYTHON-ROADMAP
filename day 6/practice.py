
#PROBLEM NO.1

# a1 = int(input("enter number 1 : " ))
# a2 = int(input("enter number 2 : " ))
# a3 = int(input("enter number 3 : " ))
# a4 = int(input("enter number 4 : " ))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("the greatest number is a1 : ", a1)
    
# elif(a2>a1 and a2>a3 and a1>a4):
#     print("the greatest number is a2 : ", a2)
    
# elif(a3>a1 and a3>a2 and a3>a4):
#     print("the greatest number is a3 : ", a3)
    
# elif(a4>a1 and a4>a2 and a4>a3):
#     print("the greatest number is a4 : ", a4)
    
# print("Found the greatest number ")      


#PROBLEM NO.2 

# marks1 = int(input("enter subject 1 marks : "))
# marks2 = int(input("enter subject 2 marks : "))
# marks3 = int(input("enter subject 3 marks : "))

# total_marks = (100)*(marks1 + marks2 + marks3)/300
# if(total_marks >=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("You are passed, and your marks percentage is :",total_marks,"%")
# else:
#     print("You are failed, and your marks percentage is :",total_marks,"%")


#PROBLEM NO.3

# p1 = "make lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# message = input("enter your comment : ")

# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("This is a spam comment")
# else:
#     print("This is not a spam comment")

#PROBLEM NO.4

# username = input("enter your name :")

# if(len(username)<10):
#     print("given username contains less than 10 characters")
# else:
#     print("given username contains more than 10 characters")

#PROBLEM NO.5

# l = ["fazil", "irfan", "chintu"]

# name = input("enter name : ")
# if(name in l):
#     print("your name is in the list")
# else:
#     print("your name is not in the list")

#PROBLEM NO.6

# marks = int(input("enter you marks: "))

# if(marks<=100 and marks>=90):
#     grade="EX"
# elif(marks<90 and marks>=80):
#     grade="A"
# elif(marks<80 and marks>=70):
#     grade="B"
# elif(marks<70 and marks>=60):
#     grade="C"
# elif(marks<60 and marks>=50):
#     grade="D"
# elif(marks<50):
#     grade="FAIL"
    
# print("your grade is : ", grade)

#PROBLEM NO.7

post = input("enter the the post : ")

if("Fazil".lower() in post.lower()):
    print("This post is talking about fazil")
else:
    print("This post is not talking about fazil ")
    