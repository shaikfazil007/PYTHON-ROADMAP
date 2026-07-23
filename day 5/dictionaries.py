#dictionaries
 
marks = {
    "fazil" : 98,
    "chintu" : 87,
    "irfan" : 22,
    "asshu" : 29
}
print(marks, type(marks))
print(marks["chintu"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"chintu":75,"rishi":99})
print(marks) 
print(marks.get("fazil"))  #retuns none
print(marks["dev"])     #returns an error



