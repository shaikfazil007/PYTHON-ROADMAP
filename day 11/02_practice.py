# PROBLEM 1
class programmer:
    company = "mocrosoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin= pin
        
p = programmer("fazil",100000,504050)
print(p.name,p.salary,p.pin,p.company)     
r = programmer("rehan",200000,505023)   
print(r.company,r.salary,r.pin,r.name)

# PROBLEM 2

class calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"the square is {self.n*self.n}")
    def cube(self):
            print(f"the cube is {self.n*self.n*self.n}")
    def squareroot(self):
            print(f"the squareroot is {self.n**0.5}")            
            
a = calculator(4)
a.square()
a.cube()
a.squareroot()       

# PROBLEM 3

class demo:
    a = 4
o = demo()
print(o.a)
o.a = 0
print(o.a)
print(demo.a)        

# PROBLEM 4

class calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"the square is {self.n*self.n}")
    def cube(self):
            print(f"the cube is {self.n*self.n*self.n}")
    def squareroot(self):
            print(f"the squareroot is {self.n**0.5}") 
    @staticmethod
    def hello():
        print("hello there !")
        
a = calculator(4)
a.square()
a.cube()
a.squareroot()
a.hello()     

# PROBLEM 5


from random import randint

class train:
       def __init__(self, trainNo,):
           self.trainNo = trainNo
       
       def book( self, fro, to):
           print(f"your ticket is booked in train no: {self.trainNo} from {fro} to {to}")
       def getStatus(self):
           print(f"train no: {self.trainNo} is running on time")    
       def getFare(self, fro, to):
           print(f"your fare in train no: {self.trainNo} from {fro} to {to} is {randint(200,1000)}") 
           
t = train(12399)       
t.book("hyderabad","mumbai") 
t.getStatus()
t.getFare("hyderabad","mumbai")      

# PROBLEM 6

from random import randint

class train:
       def __init__(slf, trainNo,):
           slf.trainNo = trainNo
       
       def book( self, fro, to):
           print(f"your ticket is booked in train no: {self.trainNo} from {fro} to {to}")
       def getStatus(self):
           print(f"train no: {self.trainNo} is running on time")    
       def getFare(self, fro, to):
           print(f"your fare in train no: {self.trainNo} from {fro} to {to} is {randint(200,1000)}") 
           
t = train(12399)       
t.book("hyderabad","mumbai") 
t.getStatus()
t.getFare("hyderabad","mumbai") 