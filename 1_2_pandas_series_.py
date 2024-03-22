# -*- coding: utf-8 -*-
"""1_2-pandas series .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fpMQ4lszujHx0Qi38oFj2rgW5wbE88lO
"""

import pandas as pd
df=pd.read_csv("/content/empdata.csv")

df.head()

df.style

df.shape

df.Empid

df.columns

df.tail(2)

df.describe

df.info()

df.size

df.Salary

df[['Empid','Ename']]

df[['Ename','DOJ']]

df[['Salary','DOJ']]

"""check for duplicates and remove them"""

df1=df.append(df)
print('Dimension of the original frame',df.shape)
print('Dimension of the frame with duplicates',df1.shape)
#remove the duplicates
df1=df1.drop_duplicates()#or use this statement df1.drop_duplicate(inplace=True)
print('dimension of the frame after after removing duplication',df1.shape)

#change all column names to upper case
df.column=[i.upper() for i in df]
print(df.columns)

df.columns=[i.upper() for i in df]
print(df.columns)

"""handling missing values"""

df.isna().sum()
#df.isnull().sum()
#print(df.isnull())
print('the no. of nulls in each column is \n',df.isnull().sum())
df.dropna(axis=1,inplace=False)

df

print('highest salary is',df['Salary'].max())
print('lowest salary is ',df['Salary'].min())

df.SALARY

df[df.SALARY>2000]

df[['EMPID','ENAME']] [df.SALARY > 20000]

df[['Empid','Ename']][df.Salary==df.Salary.max()]

"""display the enames whose salary is above the averaage salary"""

print('average Salary is',df.Salary.mean())
df['Ename'][df.Salary>df.Salary.mean()]

"""sort in ascending order of doj and store the result in another frame

"""

df1['DOJ']=pd.to_datetime(df1['DOJ'])#convert doj to data type
df1.info()
print('frame before sorting\n',df1)
df1.sort_values("DOJ",inplace=True)
print('frame after sorting\n',df1)