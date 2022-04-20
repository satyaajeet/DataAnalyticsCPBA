# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 21:06:53 2022

@author: satya
"""
#Dictonary

#mutable, non indexed, heterogenous, non unique, key value pair

d1={}


#key value pair
d2={'rno':1,'name':'Satya'}


#heterogenous
car={'brand':'Honda','color':'white','model':'jazz'}

car

car[1]

car['brand']

car['color']

car['model']

car.keys
car.keys()

car.values()

rno=list(range(1,101))
rno

stud={'rno':rno}

stud['rno']

car['year']=2020

car
car.pop('brand')
car

car.popitem()
car

car.clear()
car
del car

l1=[20,21,22,23,24]
l1

l2=l1

l1.pop()
l2.append(24)

l3=l1.copy()
l3.append(25)



#Conditions

'''
if(condition):
    {
     statement
     }
'''

a=10
b=20

if a<b:
    print('a is lesser')
    
if (0):
    print('a is lesser')
    
if(-11):
    print('a is lesser')
    
if (a<b):
    print('a is lesser')
else:
    print('a is greater')


mark=int(input('Input marks'))

if(mark>90):
    print('A')
elif(mark>80 and mark<=90):
    print('B')
else:
    print('C')


#looping

teamA=['India','Australia','Pakistan','England']

teamA[0]
teamA[1]

for i in teamA:
    print(i)
    
r1=list(range(1,11))
r1

for i in r1:
    print(i*2)

for i in r1:
    print('2 X {} = {}'.format(i,i*2))
    

j=list(range(2,6))
j

for i in range(1,11):
    print('{0} X {1} = {2}'.format(j,i,j*2))
    
    
print('hello','world',end='\n')

print('hello','world')
print('hello','world',sep='')


while(True):
    print(1)
    
while(False):
    print(1)
    
j=1
while(j<=10):
    i=1
    while(i<=10):
        print('{0} X {1} = {2}'.format(j,i,j*i))
        i=i+1
    j=j+1
    print('--------------------------')


#break
#continue

import numpy as np

a=np.random.randint(0,1000,size=100)
a

cnt=1
for i in a:
    print(cnt)
    cnt=cnt+1
    if(i==65):
        print('Number searched')
        break

for i in a:
    break


teamA

for t in teamA:
    if(t=='Pakistan'):
        print(t, 'in loop')
        break
    else:
        print(t, 'out of loop')
    
for t in teamA:
    if(t=='Pakistan'):
        print(t, 'in loop')
        continue
    else:
        print(t, 'out of loop')


pswd='satya'

while(True):
    p=input('Enter Password: ')
    if(p==pswd):
        print('Password Accepted')
        break
    print('Enter Correct password')
    continue


#functions

def op():
    a=10
    b=20
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    
op()

def op1(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

op1(10,30)


#To avoid error in parameters, define a default value

l=np.random.randint(10,200,22)

def maxnum(lst):
    n=max(l)
    return n

l=np.random.randint(10,200,22)
a=maxnum(l)

print(a)


n=int(input('Enter a mobile number'))

n=str(n)
l=len(n)
if(l==10 ):
    print('Mobile number accepted')
else:
    print('Number not accepted')

#lambda function

def f(x):
    return x**2

f(3)

f1=lambda x: x**2

f1(3)

fl=lambda x,y: x*y

fl(3,4)


#map
l1=['as','we','rt']
s=lambda x:x.upper()
list(map(s,l1))


#filter

l1=np.random.randint(1,20,size=5)
s=lambda x: x%2==0
list(filter(s,l1))
l1



