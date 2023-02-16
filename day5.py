# recursion-->when a function call itself
def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print(factorial(43))
print(factorial(1))

def nthfibonaci(n):
    if(n==0 or n==1):
        return n
    else:
        return nthfibonaci(n-1)+nthfibonaci(n-2)
print(nthfibonaci(4))
print(nthfibonaci(5))
print(nthfibonaci(6))

def fibonaci(n):
    if(n==0 or n==1):
        return n
    else:
        return fibonaci(n-1)+fibonaci(n-2)
for i in range(6):
    print(fibonaci(i))
for i in range(10):
    print(fibonaci(i))



# sets in python-->well defined collection of objects
s={2,5,4,3,2}                      #sets can't change and can't be accessed using index
print(s)                           #this will print 2 only one time

harry=set()                        #want to make empty set? use this
print(harry)

for i in s:                        #elements in set can be accessed like this but order is not maintained and do print repeated item only one time
    print(i)


# set methods
s1={1,2,3,4,5}
s2={5,6,7,8,9}
print(s1.union(s2))                #print union of set1 and set2
print(s2.union(s1))

print(s1.intersection(s2))         #print intersection of set1 and set2
print(s2.intersection(s1))

s1.update(s2)                      #s1 ke andr o sare element lao jo s2 me hai
print(s1)

# symmetric difference-->sets me se o sare element hta do jo common ho
d1={'a','b','c','d','e'}
d2={'f','g','h','d','e'}
d3=d1.symmetric_difference(d2)
print(d3)

# difference-->this will subtract the common element
d4=d1.difference(d2)               #d1-d2
print(d4)

# isdisjoint-->check if the sets have common elements or not
print(d1.isdisjoint(d2))           #print false
print(s1.isdisjoint(s2))           #print false

# issuperset-->check if the set is superset or not
d5=d1.union(d2)                    #taking union of d1 &d2
print(d5.issuperset(d1))           #print true because every element of d1 present in d5
print(d1.issuperset(d5))           #print false because every element of d1 not present in d5

# issubset-->check if the set is subset or not
print(d1.issubset(d5))             #print true because every element of d1 present in d5
print(d5.issubset(d2))             #print false because every element of d1 present in d5

#want to add element in the set? use this
d1.add(6)
d1.add(76)
print(d1)                         #print {'c', 'a', 'b', 6, 'e', 'd', 76}

#want to remove the element from the set? use this
d1.remove(6)
d1.remove(76)
print(d1)                          #print {'c', 'a', 'b', 'e', 'd'}

#we can use discard in place of remove the main difference b/w remove and discard is that remove throw an error if the element not present in the set but discard not


# pop--> used to remove random element from the set
b=d1.pop()
print(d1)
print(b)                          #show which element is popped

#want to delete entire set? use this
del d1                            #this will delete the d1 set

#want to delete all element in the set but not the set? use this
d2.clear()

#you can use all the methods of list and tuple in the set




# dictionaries
dic={
    'am':'hoon',
    'are':'hain',
    'we':'hum'
}
print(dic['are'])                     #print hain
print(dic['we'])                      #print hum
print(dic)                            #print {'am': 'hoon', 'are': 'hain', 'we': 'hum'}

#want to know all the keys in the dictionary? use this
print(dic.keys())                     #print dict_keys(['am', 'are', 'we'])

#want to know all the values in the dictionary? use this
print(dic.values())                   #print dict_values(['hoon', 'hain', 'hum'])

print(dic.items())                                                              #print dict_items([('am', 'hoon'), ('are', 'hain'), ('we', 'hum')])
for key, value in dic.items():
    print(f"the value corresponding to the key {key} is {value}")               #print
                                                                                #the value corresponding to the key am is hoon
                                                                                #the value corresponding to the key are is hain
                                                                                #the value corresponding to the key we is hum


# dictionary methods
ep1={
    122: 45,
    123: 88,
    234: 55
}
ep2={
    444:43,
    654:55,
    43:444
}
ep1.update(ep2)
print(ep1)                                   #print {122: 45, 123: 88, 234: 55, 444: 43, 654: 55, 43: 444}

#want to clear dictionary? use this
ep1.clear()
print(ep1)                                   #print {}

# want to make empty dictionary? use this
re={}

#want to remove an item from the dictionary? use this
print(ep2)                                   #print {444: 43, 654: 55, 43: 444}
ep2.pop(43)
print(ep2)                                   #print {444: 43, 654: 55}

#want to delete a dictionary? use this
del ep1

#all the methods of list and tuple can be used in this also



#for loop with else
for i in range(6):
    print(i)
else:
    print("i am out of the loop")

for i in []:
    print(i)
else:
    print("sorry no i present")

for i in range(5):
    print("iteration no. {} in for loop".format(i+1))
else:
    print("out of loop")