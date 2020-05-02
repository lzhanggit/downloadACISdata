#%%
import pandas as pd
import numpy as np
from ACISdownloader import downloader 
p = downloader(county="31109",sdate='2019-1-1',edate='2019-12-31',elems="avgt")
#p.to_csv('test_multiday_Lancaster.csv',index=False,header=True)

#df=pd.read_csv('test_multiday_Lancaster.csv',sep='\s*',names=["UID","ll","sids","state","elevation","name","date","avgt"])

p.head()
df2 = pd.DataFrame(p,columns=['date','avgt'])
print(df2)
df2.dtypes
df2["avgt"] = df2.avgt.astype(float)
df2.dtypes
#date 
df2['date']=pd.to_datetime(df2['date'],format='%Y%m%d')
#date index
df2 = df2.set_index('date')
#按月进行平均值统计
dfM=df2.resample('M').mean()
print(dfM)

#df2.set_index(["date"], inplace=True)
#df2.index = pd.to_datetime(df2.index)
#print(df2)
#df3 = df2.groupby(df2.index.month).mean()
#df3.head()
dfM.to_csv('test_temperature_monthly_mean_Lancaster.csv',index=True,header=True)
