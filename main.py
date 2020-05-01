#%%
import pandas as pd
import numpy as np
from ACISdownloader import downloader 
p = downloader(state="CT,RI",sdate='2011-8-1',edate='2011-8-30',elems="maxt,mint")
p.to_csv('test_multiday.csv',index=False,header=True)



# %%
