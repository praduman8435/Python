# typecasting
a= "1"
b= "2"
print(a+b)                #this will return 12
print(int(a)+int(b))      #this will return 3
t=12
y=54
print(t+y)                #this will return 66


# here are two types of typecasting
# 1.explicit typecasting(jo hume khud se krna pade)
# 2.implicit typecasting(jo bina kiye hi ho jaye)

# implicit typecasting
w=32
e=44.5
print(w+e)

# explicit typecasting
s= "15"
o= 7
print(int(s)+o)


# Strings
name="Rohan"
friend="Shivam"
jack='Jill'
print("Hello "+name+jack+friend)


# want to write a poem? use this
poem='''
Johny Johny yes papa,
Eating sugar ? no papa,
Telling a lie ? no papa,
Open your mouth, hahaha...
'''
print(poem)


# in python String is like an Array of a character
print(poem[4])
print(poem[3])
print(poem[9])


# let's use a for loop to print all the character in the poem
for i in poem:
    print(i)


# String slicing
names="Harry,Shubham"
print(names[0:5])
print(names[2:7])


# string methods
h="Harry"              #strings are immutable
print(len(h))
print(h.upper())       #convert to uppercase
print(h.lower())       #convert to lowercase

print(h.replace("Harry", "John"))


# split
m="$$$ Harry !!!"
print(m.split(" "))


blogHeading="introdunction to Js"
print(blogHeading.capitalize())          #first character of blogHeading will be capitalise


str1="welcome"
print(str1.center(50))                   #contain 50 spaces
print(str1.count("l"))                   #how many times l occur
print(str1.startswith("w"))
print(str1.endswith("e"))


# find                                   #its find the index of the character/words
you="Hey! what's up guys"
print(you.find("what"))
print(you.find("lid"))                   #if not present return -1


# to check alpha numeric or not
print(you.isalnum())
print(str1.isalnum())


print(you.isalpha())                     #to check alpha or not
print(you.isupper())                     #to check uppercase or not
print(you.islower())                     #to check lower or not
print(you.isprintable())                 #to check printable or not
print(you.isspace())                     #to check space present only or not
print(you.istitle())                     #to check first charachter is in uppercase or not
print(you.swapcase())                    #to swap upper to lower and lower to upper