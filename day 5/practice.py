#problem 1
words = {
    "paani":"water",
    "gaadi":"car",
    "ghar":"home"
}
word =input("enter the word that you want to know the meaning:")
print(words[word])

#problem 2

s = set()
n = input("enter a number :")
s.add(int(n))
n = input("enter a number :")
s.add(int(n))
n = input("enter a number :")
s.add(int(n))
n = input("enter a number :")
s.add(int(n))
n = input("enter a number :")
s.add(int(n))
n = input("enter a number :")
s.add(int(n))
n = input("enter a number :")
s.add(int(n))
print(s)

#problem 3

s = set()
s.add(18)
s.add("18")
print(s)

problem 4
s = set()
s.add(18)
s.add(18.0)
s.add("18")
print(s)
print(len(s))

#problem 5

s = {}
print(type(s))

#problem 6

d = {}

name = input("enter the name : ")
language = input("enter his favourite language :")
d.update({name : language})
name = input("enter the name : ")
language = input("enter his favourite language :")
d.update({name : language})
name = input("enter the name : ")
language = input("enter his favourite language :")
d.update({name : language})
name = input("enter the name : ")
language = input("enter his favourite language :")
d.update({name : language})
print(d)

#problem 7
  #the values entered later will be updated
  
#problem 8
  #nothing will happen the values can be same
  
#problem 9
s = {1, 4, "fazil", [3.9]}
 #you cant change the values in the lis which contains set S , sets are imutable