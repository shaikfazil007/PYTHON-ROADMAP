# problem 1

name = input("enter your name : ")

print(f"good night {name}")


# problem 2

letter = '''dear <|name|>
you are selected on
<|date|>'''

a = (letter.replace("<|name|>" , " fazil"))
print(a.replace("<|date|>" , "may 15 2029"))

# problem 3

line = "shiva is a  good  boy"
print(line.find("  "))



# problem 4

line = "shiva is a  good  boy"
print(line.replace("  " , "   "))



# problem 5

letter = "dear fazil,\nthis \"python\"  journey is nice. \nthanks!"
print(letter)