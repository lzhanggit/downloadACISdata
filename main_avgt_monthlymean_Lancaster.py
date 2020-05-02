#%%
import pandas as pd
import numpy as np
from ACISdownloader import downloader 
#Question 1
p1 = downloader(sids="KCAR",sdate='2019-1-1',edate='2019-12-31',elems="avgt")
p1.to_csv('Q1_test_multiday_KCAR_station.csv',index=False,header=True)


#Question 3
format1=lambda x:"%.1f"%x
p2 = downloader(county="31109",sdate='2019-1-1',edate='2019-12-31',elems="avgt")
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
dfM=df2.resample('M').mean()
dfM[['avgt']]=dfM[['avgt']].applymap(format1)
print(dfM)
dfM.to_csv('Q3_test_temperature_monthly_mean_Lancaster.csv',index=True,header=True)
