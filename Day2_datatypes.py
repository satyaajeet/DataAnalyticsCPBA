# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 21:10:48 2022

@author: satya
"""
a=input("Enter a : ")

s="hi"
b=10
c=12.4
 
x=input("Enter a number: ")
y=input("Enter a number: ")

x= int(input("Enter a number: "))

y=int(input("Enter a number: "))


a=20
type(a)


str="My name is "
s="satya"
str+s


c="A"
ord(c)


i=65
chr(i)


test='AxSdrFGhjITa'
t=''
for i in test:
    if(ord(i)>=65 and ord(i)<=90):
        t=t+i
        
t




x=10

print(x+1)

print(x-1)

print(x*3)

print(x/2)

print(x**2)

print(x**(0.5))

print(x%3)


h='hello'
w='world'

h+w

h+ " " + w


h.capitalize()

h.upper()

h.lower()

s="Hello Java"

s.replace("Java","Python")

name=input('Enter a name: ')

name=name.strip()




# Combinational/Extended  Datatypes

#list,set,Dictionary,tuple
#mutable,indexed,ordered,heteregenous,unique values, key-value pair

l1=[]

l2=[1,2,3,4,5,6]
l3=[3 4 5 6]

#indexed

l2[0]
l2[1]

l2[6]


#Heterogenuos

l4=[10,12.4,True,'Name']

#mutable changeable

l4[1]=11

r1=range(5)
r1
r2=list(range(10))
r2

r3=list(range(11,20))
r3

r4=list(range(10,50,5))
r4


r2.append([10,12])

r2

r2.extend([11,12])
r2

r2.pop(13)

r2.remove([10,12])
r2

r2.reverse()
r2

r2.sort()


#Set

##non mutable,non indexed,ordered,heteregenous,unique values, non key-value pair

s1={10}

s2={40,20,30,10,50}
s2

s3={10,30,50,20,10,40,20}
s3

s4={"VK",10,43.2,True}
s4

s3.add(60)
s3

s3.update([10,30,60,70,80])
s3

s3.pop()
s3

s3.discard(80)
s3

s3.discard(80)
s3



teamA={'India','Australia','Pakistan','England'}
teamB={'Kenya','India','West Indies','New Zealand'}

teamA
teamB

teamA.union(teamB)
teamA.intersection(teamB)
teamA.difference(teamB)

teamA+teamB

#Tuple

t1=(1,2,3,4,5)
t2=("Name",1,2,3,4.5)

t1[1]=3

t1[0].remove()

t1.extend(5)
