# PROBLEM 1
# class programmer:
#     company = "mocrosoft"
#     def __init__(self,name,salary,pin):
#         self.name = name
#         self.salary = salary
#         self.pin= pin
        
# p = programmer("fazil",100000,504050)
# print(p.name,p.salary,p.pin,p.company)     
# r = programmer("rehan",200000,505023)   
# print(r.company,r.salary,r.pin,r.name)

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