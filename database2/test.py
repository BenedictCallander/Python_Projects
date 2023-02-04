from datetime import datetime
import time
import matplotlib.pyplot as plt 
import pandas as pd 
import glob


def history_plot():
    files=glob.glob("stockbackup/*.csv")
    combine=[]
    ex=pd.read_csv(files[1])
    names=list(ex['name'])
    for i in range(len(files)):
        df=pd.read_csv(files[i])
        combine.append(df)
    final=pd.concat(combine)
    final.sort_values(by='datetime')
    plt.figure()
    for name in names:
        dft=final.copy()
        dft=dft[dft['name'].isin([name])]
        plt.plot(dft['datetime'],dft['stock'],label=str(name))
    plt.legend(loc="upper right")
    plt.show()

history_plot()