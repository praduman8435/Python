import time

# taking input from the user
a = int(input("enter your age: "))
print("your age is: ", a)

# if else statement
if(a>=18):
    print("you can drive")
else:
    print("you can't drive")


b = int(input("enter to check even: "))
print("your no. is: ", b)

# if else statement
if(b%2==0):
    print("even")
else:
    print("odd")


# good morning program
timenow = time.strftime('%H:%M:%S')            #shows what time is in your laptop
print(timenow, "baj gye hai")                  #print what time is in your laptop
timenow = int(time.strftime('%H'))
if(timenow>5 and timenow<=12):
    print("Good Morning")
elif(timenow>12 and timenow<=15):
    print("Good Afternoon")
elif(timenow>15 and timenow<=20):
    print("Good Evening")
else:
    print("Good Night")


# match case statement(just like switch case statement)
w= input("Enter the value of x: ")
match w:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:                                    #default case
        print("enter no. between 1 to 7")


# loops in python
name = input("enter your name: ")
for i in name:
    print(i)


color = ["red", "blue", "green", "yellow"]
for i in color:
    print(i)
    for j in i:
        print(j)


n = 7
for i in range(n):                   #print no. from 1 to n-1
    print(i)

for i in range(1, 10):               #print no. from 1 to 9
    print(i)

for i in range(1, 10, 2):            #print no. from 1 to 9 with a gap of 2
    print(i)


# prime no. program
n= int(input("enter the no. to check prime: "))
count=0
for i in range(1, n+1):
    if(n%i==0):
        count+=1
if(count>2):
    print("no. is not prime")
else:
    print("no. is prime")


# while loop
m=0
while(m<10):
    print(m)
    i+=1


#break and continue statement
for i in range(10):
    if(i==5):
        break
    print(i)


for j in range(10):
    if(j==5):
        continue
    print(j)


# printing table
n= input("enter the no. you want table: ")
for i in range(11):
    print(n," X ",i+1,"=",n*(i+1))