#%%
import pandas as pd
import numpy as np
from ACISdownloader import downloader 
<<<<<<< HEAD
p = downloader(state="CT,RI",sdate='2011-8-1',edate='2011-8-30',elems="maxt,mint")
p.to_csv('test_multiday.csv',index=False,header=True)
=======
p = downloader(state="NE",sdate="2019-7-1",edate="2019-12-31",elems="maxt")
p.to_csv('test2.csv',index=False,header=True)
>>>>>>> 0ef7947ab49e8b083a9ff59385512dd6bc085e26



# %%
