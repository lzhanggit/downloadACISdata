#%%
import pandas as pd
import numpy as np
from ACISdownloader import downloader 
p = downloader(state="NE",sdate="2019-7-1",edate="2019-12-31",elems="maxt")
p.to_csv('test2.csv',index=False,header=True)



# %%
