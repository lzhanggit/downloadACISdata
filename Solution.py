""" 
		This function was coded and modified by Ligang Zhang for class project

		May 1, 2020
"""
import pandas as pd
import numpy as np
from ACISdownloader import downloader 
format1=lambda x:"%.1f"%x
#Question 1
p1 = downloader(sids="KCAR",sdate='2019-1-1',edate='2019-12-31',elems="avgt")
p1.to_csv('Q1_test_multiday_KCAR_station.csv',index=False,header=True)

#Question 2
p2 = downloader(sids="KCAR",sdate='2019-1-1',edate='2019-12-31',elems="avgt")
p2.head()
df2 = pd.DataFrame(p2,columns=['date','avgt'])
print(df2)
df2.dtypes
df2["avgt"] = df2.avgt.astype(float)
df2.dtypes
#date format
df2['date']=pd.to_datetime(df2['date'],format='%Y%m%d')
#date index
df2 = df2.set_index('date')
#monthly mean
df5D=df2.resample('5D').mean()
df5D[['avgt']]=df5D[['avgt']].applymap(format1)
df5D.columns = ['Mean Temperature (F)']
print(df5D)
df5D.to_csv('Q2_test_temperature_5day_mean_KCAR_station.csv',index=True,header=True)

#Question 3
p3 = downloader(county="31109",sdate='2019-1-1',edate='2019-12-31',elems="avgt")
p3.head()
df3 = pd.DataFrame(p3,columns=['date','uid','avgt'])
print(df3)
df3.dtypes
df3["avgt"] = df3.avgt.astype(float)
df3.dtypes
#date format
df3['date']=pd.to_datetime(df3['date'],format='%Y%m%d')
#date index
df3 = df3.set_index('date')
#monthly mean
dfM=df3.resample('M').mean()
dfM[['avgt']]=dfM[['avgt']].applymap(format1)
dfM['uid']=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
dfM.columns = ['Month','Mean Temperature (F)']
print(dfM)
dfM.to_csv('Q3_test_temperature_monthly_mean_Lancaster.csv',index=True,header=True)
