#%%
import pandas as pd
import numpy as np
from ACISdownloader import downloader 
p = downloader(state="CT,RI",date="2011-8-2",elems="maxt,mint")
p.to_csv('test.csv',index=False,header=True)


# %%
