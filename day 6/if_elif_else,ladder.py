a =int(input("enter your age : "))
if(a>=18):
    print("you can drive the vehicle")
elif(a<0):
    print("invalid negative age")
elif(a==0):
    print("you are entering an invalid age")
else:
    print("you can't drive the vehicle")
    
print("This is the 'RTO' rule ")    