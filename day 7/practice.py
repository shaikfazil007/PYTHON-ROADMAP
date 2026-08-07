# PROBLEM 1

n = int(input("enter a number : "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

# PROBLEM 2

l = ["fazil","irfan","chintu","faizaan"]
for name in l:
    if(name.startswith("f")):
        print(f"hello {name}")

# PROBLEM 3

n = int(input("enter a number : "))

i = 1
while(i<11):
    print(f"{n} x {i} = {n*i}")
    i = i+1
    
#  PROBLEM 4
    
n = int(input("enter a number : "))

for i in range (2,n):
    if(n%i) == 0:
        print("the number is not prime")
        break
else:
        print("the number is prime")

# PROBLEM 5

n = int(input("enter a number : "))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)


# PROBLEM 6 

# FACTORIAL = (5! : 1X2X3X4X5)

n = int(input("enter a number : "))
product = 1
for i in range (1,n+1):
    product = product*i
print(f"the factorial of {n} is {product}")

# PROBLEM 7

n =int(input("enter a number : "))
for i in range(1, n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")
    
n= int(input("enter a number : "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")
           
           
# PROBLEM 8

n = int(input("enter a number :"))
for i in range (1,n+1):
    print("*"*i,end="")
    print("")


# PROBLEM 9

n = int(input("enter a number : "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")

# PROBLEM 10

n=int(input("enter a number :"))
for i in range (1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")