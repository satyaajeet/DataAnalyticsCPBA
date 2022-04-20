# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 21:04:03 2022

@author: satya
"""
import pandas as pd

from pydataset import data

data()

mt=data('mtcars')

type(mt)
 mt

mt.to_csv('mt_cars.csv',index=True)

import pandas as pd

df=pd.read_csv('mt_cars.csv')

df.tail()

df.head()
df.shape
df.dtypes

s=pd.Series(range(1,11))
s
s1=pd.Series(['a','b','c','d','e'])
s1

ps1=pd.Series([100,200,300,400,500],index=['a','b','c','d','e'])
ps1

ps1['a']
ps1.loc['b']
ps1.iloc[0]
ps1[1]


ps1.index
ps1.values

import numpy as np
ps4=pd.Series(np.random.randint(1,100,size=10))
ps4

ps4>30
ps4[ps4>30]

import pandas as pd

course=pd.Series(['MBA','BBA','Btech','Mtech'])
strength=pd.Series([100,200,400,300])
fees=pd.Series([1.7,1.2,1.8,1.9])

dic={'Course':course,'Strength':strength,'Fees':fees}
dic
df=pd.DataFrame(dic)
df.to_csv('CD.csv')
df.keys

df.Course

df.loc[1:3]

df.iloc[:2]

df.Course=='BBA'

df[df.Course=='BBA']

df[[True,True,False,False]]


#Missing Data

import pandas as pd
import numpy as np

placed=pd.Series([None,np.nan,100,None])

df['Placed']=placed

df

df.dropna(axis=1)
df.dropna(axis=0)


df.dropna(axis='rows')
df.dropna(axis='columns')



df.dropna(axis='rows',how='any')
df.dropna(axis='columns',how='all')

df.dropna(axis='columns',thresh=2)

df.fillna(0)
df['Course'].fillna(7)

df.fillna(method='ffill') #forward fill
df.fillna(method='bfill') # backward fill




df.notnull()
df.isnull()

x=[[1,2,3],[3,4,5]]
y=[[10,11,12],[13,14,15]]

np.concatenate([x,y],axis=1)

grades1={'subject1':['A1','A2','A3'],'subject2':['B1','A2','A3','B2']}




#Synthetic Dataset

import pandas as pd
import numpy as np
rno=pd.Series(range(1001,1011))
rno
'''
name=[]
for i in range(1,11):
    name.append('Student'+str(i))
    
name
'''

name=['Student'+ str(i) for i in range(1,11)]

name

gl=['M','F']

gender=np.random.choice(a=gl,size=10)
gender

course=np.random.choice(['MBA','Mtech','Btech','PhD'],size=10)
course

marks=np.random.choice(a=range(1,101),size=10)
marks

stud=pd.DataFrame({'RNO':rno,'NAME':name, 'GENDER':gender,'COURSE':course,'MARKS':marks})
stud

fees=pd.DataFrame({'COURSE':['MBA','Mtech','Btech','PhD'],'fees':[150000,1300000,1700000,2000000]})

df=pd.merge(stud,fees)
df
