import customtkinter as Ctk
from tkinter import * 
from tkinter import ttk
import uuid 
import csv
import sqlite3
import glob
import pandas as pd 
from pandastable import Table
from datetime import datetime
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from buttons import buttons

root = Tk()


p1 = PhotoImage(file = 'icon.png')
root.geometry("1280x720")
root.title("Bedrock Inventory Management")
root.iconphoto(False, p1)
root.configure(bg="#2E2E2E")
back = PhotoImage(file = "bedrock.png")
label1= Label(root,image=back,bg="#2E2E2E")
label1.grid(row=0,column=5)
title=Label(root, text="Inventory Management V 0.1",font=("Helvetica", 20),bg="#2E2E2E",fg="#F38060")
statement = Label(root, text="Benedict Callander 2023",bg="#2E2E2E",fg="#F38060")

title.grid(row=0, column=1)
statement.grid(row=1, column=1)

button1 = Button(root, text="Add Stock",bg='red', command=buttons.add, padx=50, pady=50)
button2 = Button(root, text="Adjust stock",bg='blue', command= buttons.adjust, padx=50, pady=50)
button3 = Button(root, text="System Stock",bg='green',command=buttons.see_systems, padx=50, pady=50)
button4 = Button(root, text="View Inventory",bg='orange',command=buttons.component_list, padx=50, pady=50)
button5 = Button(root, text="pricechange(defunct)",bg='#C35F40', padx=50, pady=50)
button6 = Button(root, text="Used-sys-import",bg='#F38060',command=buttons.usedsys, padx=50, pady=50)
button7 = Button(root, text="Stock-Backup (defunct)",bg='#F38060', padx=50, pady=50)
button8 = Button(root, text="Stock-Backup(defunct)",bg='#F38060', padx=50, pady=50)
button1.grid(row=2, column=2)
button2.grid(row=2, column=3)
button3.grid(row=2, column=4)
button4.grid(row=3, column=2)
button5.grid(row=3, column=3)
button6.grid(row=3, column=4)
button7.grid(row=4,column=1)
button8.grid(row=4, column=2)


#stock_backup()
root.mainloop()