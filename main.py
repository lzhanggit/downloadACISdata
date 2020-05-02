#%%
import pandas as pd
import numpy as np
from ACISdownloader import downloader 
p = downloader(county="31109",sdate='2011-1-1',edate='2011-12-31',elems="maxt,mint")
p.to_csv('test_multiday2.csv',index=False,header=True)



# %%
