# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:54:57 2022

@author: satya
"""
import this

import pandas as pd

from pydataset import data

data()

mt=data('mtcars')

mt

type(mt)

mt.to_csv('mtcars.csv',index=False)

df=pd.read_csv('mtcars.csv')
df

df.comtcars
df.head()

df.dtypes

s=pd.Series(range(1,11))
s
s

s1=pd.Series(['a','b','c','d','e'])
s1

ps1=pd.Series([100,200,300,400,500],index=[1,4,3,6,7])
ps1

ps2=pd.Series([100,200,300,400,500],index=['a','b','c','d','e'])
ps2

ps2['b']

ps2.loc['b']

ps2.iloc[0]

import numpy as np

ps4=pd.Series(np.random.randint(1,100,size=10))
ps4

ps4>30
ps4[ps4>30]

ps4[(ps4>30) & (ps4<70)]


course=pd.Series(['Btech','Mtech','MBA','BBA'])
strength=pd.Series([100,250,200,150])
fees=pd.Series([1,1.5,1.7,1.2])

course
strength
fees

dic={'Course':course,'Strength':strength,'Fees':fees}
dic

df=pd.DataFrame(dic)
df

df.to_csv('CD.csv')

df

df.keys()

df.columns

df['Course']
df.Course

df.index=df.Course
df

df.drop('Course',axis=1)

df=pd.DataFrame(dic)
df

df.Course=='MBA'

df[df.Course=='MBA']

df[(df.Course=='MBA') | (df.Course=='BBA')]

df[[False,False,True,True]]

import pandas as pd
import numpy as np

placed=pd.Series([None,np.nan,100,None])
placed

df['Placed']=placed

df
df.dropna()

pd4 = pd.DataFrame([['dhiraj', 50, 'M', 10000, None], [None, None, None, None, None], ['kanika', 28, None, 5000, None], ['tanvi', 20, 'F', None, None], ['poonam',45,'F',None,None],['upen',None,'M',None, None]])

pd4

pd4.dropna(axis='rows',thresh=3)

pd4.fillna(0)
pd4.fillna(10)
pd4[1].fillna(10)


data()
from pydataset import data
air=data('AirPassengers')
air

air.plot(kind='line',x='time',y='AirPassengers')

air.plot(kind='line')

air

np.random.randint(0,111,size=10)

air1=air['AirPassengers'].loc[np.random.randint(0,111,size=10)]=np.nan
air1

air['AirPassengers'].iloc[np.random.randint(0,111,size=10)]=np.nan
air

air.fillna(0).plot()
air.fillna(method='ffill').plot()


mt
mt.columns

ch=mt.columns

ch
ch=list(ch)
ch

c=np.random.choice(a=ch,size=5)
c
len(ch)

np.random.randint(1,32,size=7)

for i in c:
    mt[i].iloc[np.random.randint(1,32,size=7)]=np.nan
    
mt

mt.isnull()

mt.isnull().sum(axis=1)
mt.isnull().sum()

mt.hp

mt.std()
mt.var()
mt.max()
mt.min()
mt.sum()


x=[[1,2,3],[4,5,6]]
y=[[11,12,13],[14,15,16]]

np.concatenate([x,y],axis=1)

#Synthetic data

def crdata(gl,cl,fees):
    rno=list(range(1,100001))
    name=['Student'+str(i) for i in range(1,100001)]
    course=np.random.choice(a=cl,size=100000)
    gender=np.random.choice(a=gl,size=100000)
    marks=np.random.randint(1,101,size=100000)
    stud=pd.DataFrame({'RNO':rno,'NAME':name,'GENDER':gender,'COURSE':course,'MARKS':marks})
    pd.merge(stud,fees)
    stud.to_csv('first_data_creation.csv',index=False)
    return None


gl=['M','F']
cl=['MBA','BBA','Btech','Mtech']
fees=pd.DataFrame({'COURSE':['MBA','BBA','Mtech','Btech'],'FEES':[20,5,15,10]})
crdata(gl,cl,fees)


stud=pd.read_csv('first_data_creation.csv')
stud.head()

stud['GENDER'].value_counts().plot(kind='bar')
stud['COURSE'].value_counts().plot()

stud['MARKS'].value_counts().plot(kind='bar')

fees=pd.DataFrame({'COURSE':['MBA','BBA','Mtech','Btech'],'FEES':[20,5,15,10]})

stud
pd.merge(stud,fees)
