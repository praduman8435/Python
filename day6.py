# exception handling
a= input('enter the no. to print the table: ')
try:
    for i in range(1, 11):
      print(f"{int(a)} X {int(i)} = {int(a)*i}")
except:
    print('invalid input')
print('revenge')
# when you enter any string now then this program will show error to handle that we use exception handling


# finally keyword --> this will always be executed
try:
    m=[3,5,4,6]
    i=int(input('enter the index: '))
    print(m[i])
except:
    print('some error occured')
finally:
    print('i will always executed')


#raising custom error in python
# a= int(input('Enter any value between 5 to 9: '))
# if(a<5 or a>9):
#     raise ValueError('value should be in between 5 to 9')


#short hand if else
a=99
b=65
print('a') if a>b else print('=') if a==b else print('b')


#enumerate function in python
index=0
marks=[4,5,43,66,23,45]
for i in marks:
    if(index==3):
      print('awesome')
    index+=1

m=0
for m, i in enumerate(marks):
    print(i)
    if(m==3):
        print('ullu')