
# PROBLEM 1

def greatest():
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = 20
b = 30
c = 40
    
print(greatest()) 

# PROBLEM 2

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("enter temperature in f : "))
c = f_to_c(f)
print(f"{round(c,2)}°C ")

# PROBLEM 3

print("a")
print("b")
print("c", end = "")
print("d", end = "")
print()

# PROBLEM 4

def sum(n):
    if (n==1):
        return 1
    return sum(n-1)+n
n = int(input("enter a number : "))
print(f"the sum is : {sum(n)}")

# PROBLEM 5

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)
    
pattern(10)

# PROBLEM 6

def inch_to_cm(inch):
    return inch * 2.54
n = int(input("enter number in inches :"))
print(f"the corresponding value in cm is: {inch_to_cm(n)}")

# PROBLEM 7

def rem(l,word):
    n=[]
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n
l = ["fazil", "rohan","shubham","an"]
print(rem(l,"an"))        
        
# PROBLEM 8        

def multiply(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
        
multiply(7)                