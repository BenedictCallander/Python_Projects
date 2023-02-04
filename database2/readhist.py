import pandas as pd 
import numpy as np 
import glob 
import os
import matplotlib.pyplot as plt 
files = glob.glob("stockbackup/*.csv")
files.sort(key=lambda x: os.path.getmtime(x))
print(files)
times=[]
stock_hist=[]
for i in range(len(files)):
    df=pd.read_csv(files[i])
    values=list(df['stock'])
    names=list(df['name'])
    



for i in range(len(values)):
    plt.plot(times,values[1],label=str(names[1]))
    plt.legend(loc="upper right")
plt.show()
plt.close()