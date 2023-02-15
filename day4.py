import math

# function
def Average(a,b):
    avg=(a+b)/2
    print(avg)

Average(3, 4)
Average(2, 89)


def isGreater(a,b):
    if(a>b):
        print(a, 'is greater')
    else:
        print(b, 'is greater')

isGreater(4,6)
isGreater(9,6)


def average(*numbers):         #takes no. as a tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum/len(numbers))

average(5,6)
average(7,5,9,7,44,3)


# list-->ordered collection of data
l= [3,5,2]
print(l)
print(l[0])
print(l[2])

s=[3,5,"hii",True]
print(s[0])
print(s[3])
print(s[2])
print(s[-3])
print(s[len(s)-3])


if 5 in s:                  #finding a number in a list
    print("yes")
else:
    print("no")

if "ello" in "hello":       #finding the sting in a list
    print('yes')
else:
    print('no')


print(s)
print(s[::2])                     #print with a jump of 2
print(s[1:])                      #print from index 1 to len(s)
print(s[::-1])                    #to print in reverse


# list comprehension
a=[i for i in range(5)]
print(a)

b=[i*3 for i in range(10) if i%2==0]
print(b)


# list methods
l=[1,6,76,55,3,3,3,5,7]
print(l)

l.append(9)                 #this will add in the list of l at last
print(l)

l.sort()                    #this will short the list in ascending order
print(l)

l.sort(reverse=True)        #this will short the list in descending order
print(l)

l.reverse()                 #this will reverse the list
print(l)

print(l.index(55))          #this show the index of 55 in the list

print(l.count(3))           #this will show how many times the 3 occur in the list

m=l
m[0]=0                      #this wil change the value of index 0 in the list l
print(l)

n=l.copy()                  #this will copy the elements of l in the n
n[0]=9                      #this will change the value at index 0 only in the list n and l remains the same
print(l)
print(n)

l.insert(2,175)            #if you want to insert the value at any index in the list
print(l)
l.insert(4,666)
print(l)

h=[4,65,77]
l.extend(h)                #this will add the elements of h in l
print(l)


#tuple methods
countries= ("france","italy","india","usa")
temp= list(countries)                    #making new list and putting all elements of countries in it
temp.append("russia")                    #add
temp.pop(3)                              #remove
temp[2]="china"                          #change
countries=tuple(temp)
print(countries)

desh1=("ram","shyam","ghanshyam")
desh2=("raju","raju","punam","radha")
desh= desh1 + desh2                     #adding to tuples
print(desh)

b= desh.count("raju")                   #to check how many times raju present in the tuple
print(b)

n= desh.index("raju")                   #show the index of raju in desh
print(n)

print(len(desh))                        #show the length of desh tuple



#f-strings-->used for string formating
letter ="hey! my name is {} and i'm from {}"
name= "Raj"
country= "india"
print(letter.format(name,country))           #this will put name in 1st {} and countyr in 2nd {}

# instead of doing this you can do this f-string
print(f"Hey! humara name {name} hai aur mai {country} country se hu")

print(f"{2*30}")                             #this will print 60 but its type is string

print(f"Hey! humara name {{name}} hai aur mai {{country}} country se hu")          #if you want to print {}


#docstring-->used for documentation in code it can be written just below the function
def square(n):               #function that print square
    '''takes in the no. n and returns square of it'''          #docstring
    print(n**2)
square(5)

print(square.__doc__)                 #print the square value with docstring


# pep8-->provide best guidlines and practice for python
#full form is (python enhancement proposal)

# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!