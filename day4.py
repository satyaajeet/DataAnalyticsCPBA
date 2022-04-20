# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 20:59:24 2022

@author: satya
"""

print('Satya')

import random as rd

r1=rd.randint(1,100)
r1

r2=rd.randrange(0,10)
r2

l1=list(range(100))
l1

l2=rd.choices(l1,k=10)
l2

r3=rd.randint(0,100,10)
r3


import numpy as np

r1=np.random.randint(10)
r1

type(r1)

r2=np.random.randint(10,100)
r2

type(r2)

#1dim
r3=np.random.randint(10,100,size=9)
r3

type(r3)

#2dim

r4=np.random.randint(10,100,size=[3,4])
r4
r4.shape
r4=r4.reshape(1,12)
r4
type(r4)

r5=np.random.randint(10,100,size=[8,10])
r5

#3dim

r6=np.random.randint(10,100,size=[2,3,4])
r6

#4dim

r7=np.random.randint(10,100,size=[2,3,4,5])
r7

r7.shape

r8=np.random.randint(10,100,size=[4,5])
r8

r8[1:3,1:3]
r8[-1,-1]

r8[-1,-2:]


r9=np.random.randint(10,100,size=[2,3,4])
r9

r9[:,1:3,1:3]

r10=np.random.randint(10,30,size=(4,5))
r10

r10[:,::2]


####################################################

import numpy as np
a1=np.arange(10)
a1

a2=np.arange(10,20,5)
a2

a4=np.zeros((3,4))
a4

a5=np.ones((3,3))
a5

a6=np.eye(3)
a6

a7=np.linspace(0,10,num=8)
a7

n=np.random.randint(10,50,size=(4,5))
n

np.sum(n)

np.mean(n)
np.var(n)
np.std(n)
np.mean(n,axis=1)

np.floor([1.2,1.6])
np.ceil([1.2,1.6])
np.round([1.2,1.6])
np.trunc([-1.2,1.6])

np.round([1.2343535,1.24342525],3)


n1=np.random.randint(20,30,size=(3,4))
n2=np.random.randint(10,20,size=(3,4))
n4=np.concatenate([n1,n2],axis=0)
n4
n5=np.split(n4,2,axis=1)
n5

n6=np.random.randint(0,100,size=100)
n6
n6>30

np.all(n6>30)
np.any(n6>10)
np.sum(n6<10)

n7=np.array([4,7,np.nan,np.nan])
n7

n6
n6.sort()
n6

n8=np.random.randint(1,10,size=50)
n8

np.sum((n8>4)&(n8<8))



#Pandas

import matplotlib.pyplot as plt
import numpy as np

l1=np.random.randint(1,10,size=1000)

plt.hist(l1)
np.mean(l1)
np.sum(l1)
np.std(l1)
    
l2=np.random.normal(10,1,size=10000)

plt.hist(l2)
np.mean(l2)
np.sum(l2)
np.std(l2)
    
l3=np.random.binomial(1,p=.2  ,size=100)
plt.hist(l3)

l4=np.random.poisson(0.9,size=1000)
plt.hist(l4)

l5=np.random.uniform(0,10,size=100)
plt.hist(l5)

l6=np.random.exponential(0.9,size=100)
plt.hist(l6)


p=reversed(list(range(10,1,-1)))
p
