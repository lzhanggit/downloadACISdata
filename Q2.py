# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:21:11 2020

@author: LZHome
"""


import pandas as pd
import numpy as np
from ACISdownloader import downloader 
format1=lambda x:"%.1f"%x

#Question 2
p2 = downloader(county="31109",sdate='2019-1-1',edate='2019-12-31',elems="avgt")
p2.head()
pnew = pd.DataFrame(p2)
#date format
pnew['date']=pd.to_datetime(pnew['date'],format='%Y%m%d')
#date index
pnew2 = pnew.set_index('date')
#print(pnew2)
s1 = pnew2.loc[pnew2['uid']==12474]
print(s1)
s2 = pnew2.loc[pnew2['uid']==12527]
print(s2)
s3 = pnew2.loc[pnew2['uid']==31731]
print(s3)
s4 = pnew2.loc[pnew2['uid']==31732]
print(s4)
s5 = pnew2.loc[pnew2['uid']==85592]
print(s5)

#CRETE 4ESE
dfs1name = pd.DataFrame(s1,columns=['name'])
dfs1 = pd.DataFrame(s1,columns=['date','avgt'])
dfs1["avgt"] = dfs1.avgt.astype(float)
dfs1['date']=pd.to_datetime(dfs1['date'],format='%Y%m%d')
df5Ds1 = dfs1.resample('5D').mean()
df5Ds1[['avgt']]=df5Ds1[['avgt']].applymap(format1)
df5Ds11 = pd.merge(dfs1name,df5Ds1,on='date')
df5Ds12 = df5Ds11.reset_index(drop=False)
df5Ds12.drop_duplicates('date','first',inplace = True)
print(df5Ds12)
#LINCOLN AIRPORT
dfs2name = pd.DataFrame(s2,columns=['name'])
dfs2 = pd.DataFrame(s2,columns=['date','avgt'])
dfs2["avgt"] = dfs2.avgt.astype(float)
dfs2['date']=pd.to_datetime(dfs2['date'],format='%Y%m%d')
df5Ds2 = dfs2.resample('5D').mean()
df5Ds2[['avgt']]=df5Ds2[['avgt']].applymap(format1)
df5Ds21 = pd.merge(dfs2name,df5Ds2,on='date')
df5Ds22 = df5Ds21.reset_index(drop=False)
df5Ds22.drop_duplicates('date','first',inplace = True)
print(df5Ds22)
#LINCOLN 8 ENE
dfs3name = pd.DataFrame(s3,columns=['name'])
dfs3 = pd.DataFrame(s3,columns=['date','avgt'])
dfs3["avgt"] = dfs3.avgt.astype(float)
dfs3['date']=pd.to_datetime(dfs3['date'],format='%Y%m%d')
df5Ds3 = dfs3.resample('5D').mean()
df5Ds3[['avgt']]=df5Ds3[['avgt']].applymap(format1)
df5Ds31 = pd.merge(dfs3name,df5Ds3,on='date')
df5Ds32 = df5Ds31.reset_index(drop=False)
df5Ds32.drop_duplicates('date','first',inplace = True)
print(df5Ds32)
#LINCOLN 11 SW
dfs4name = pd.DataFrame(s4,columns=['name'])
dfs4 = pd.DataFrame(s4,columns=['date','avgt'])
dfs4["avgt"] = dfs4.avgt.astype(float)
dfs4['date']=pd.to_datetime(dfs4['date'],format='%Y%m%d')
df5Ds4 = dfs4.resample('5D').mean()
df5Ds4[['avgt']]=df5Ds4[['avgt']].applymap(format1)
df5Ds41 = pd.merge(dfs4name,df5Ds4,on='date')
df5Ds42 = df5Ds41.reset_index(drop=False)
df5Ds42.drop_duplicates('date','first',inplace = True)
print(df5Ds42)
#Rogers Farm #1
dfs5name = pd.DataFrame(s5,columns=['name'])
dfs5 = pd.DataFrame(s5,columns=['date','avgt'])
dfs5["avgt"] = dfs5.avgt.astype(float)
dfs5['date']=pd.to_datetime(dfs5['date'],format='%Y%m%d')
df5Ds5 = dfs5.resample('5D').mean()
df5Ds5[['avgt']]=df5Ds5[['avgt']].applymap(format1)
df5Ds51 = pd.merge(dfs5name,df5Ds5,on='date')
df5Ds52 = df5Ds51.reset_index(drop=False)
df5Ds52.drop_duplicates('date','first',inplace = True)
print(df5Ds52)

dfcounty = pd.concat( [df5Ds12, df5Ds22, df5Ds32, df5Ds42,df5Ds52], axis=0 )
print(dfcounty)
dfcounty.columns = ['date','station name','Mean Temperature (F)']
print(dfcounty)

dfcounty.to_csv('Q2_mutistation5Daymean.csv',index=False,header=True)