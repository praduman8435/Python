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