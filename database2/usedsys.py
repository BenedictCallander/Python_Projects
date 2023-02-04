import sqlite3
from tkinter import * 
import uuid
import pandas as pd 
import time
root=Tk()

import sqlite3
import pandas as pd
from datetime import datetime

dt=datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
print(dt)
tstamp=datetime.today().strftime('')
# Connect to the database file
conn = sqlite3.connect("stock.db")

# Read data from the table into a pandas dataframe
df = pd.read_sql_query("SELECT * FROM stock", conn)
df['datetime']=time.time()
# Close the connection to the database
conn.close()




# Write the dataframe to a CSV file
df.to_csv("stockbackup/{}.csv".format(dt), index=False)
