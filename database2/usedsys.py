import sqlite3
from tkinter import * 
import uuid
import pandas as pd 

root = Tk()
root.geometry("300x150")
root.configure(bg="#F18E0F")
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=2)
root.columnconfigure(2,weight=2)

def addsys():
    man = str(e_man.get())
    cpu = str(e_CPU.get())
    psu = str(e_PSU.get())
    ram = str(e_RAM.get())
    sys= pd.DataFrame({"Manufacturer":man, "CPU": cpu, "PSU": psu, "RAM":ram},dtype="string")
    sysID = uuid.UUID4()
    fpath="{}.csv".format(sysID)
    sys.to_csv(fpath)
    e_man.delete(0,END)
    e_CPU.delete(0,END)
    e_PSU.delete(0,END)
    e_RAM.delete(0,END)


l_man= Label(root, text="Manufacturer",bg="#F18E0F")
e_man = Entry(root)


l_CPU = Label(root, text="CPU",bg="#F18E0F")
e_CPU = Entry(root)

l_PSU = Label(root, text="PSU Wattage",bg="#F18E0F")
e_PSU = Entry(root)

l_RAM = Label(root, text="Ram Size",bg="#F18E0F")
e_RAM = Entry(root)

l_man.grid(row=1, column=1,sticky=W);e_man.grid(row=1, column=2,columnspan=2)
l_CPU.grid(row=2, column=1,sticky=W);e_CPU.grid(row=2, column=2,columnspan=2)
l_PSU.grid(row=3, column=1,sticky=W); e_PSU.grid(row=3, column=2,columnspan=2)
l_RAM.grid(row=4, column=1,sticky=W); e_RAM.grid(row=4,column=2,columnspan=2)

save_button = Button(root, text="Add System",bg="#2E2E2E",fg="orange",command=addsys)
save_button.grid(row=5, column=2, sticky=SE,padx=5,pady=5)

root.mainloop()