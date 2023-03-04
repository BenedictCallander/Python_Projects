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


class buttons:
    def add():
        win = Toplevel()
        win.title("Add Component")
        win.geometry("500x500")

        #Create input fields and labels
        brandtxt=Label(win, text="Brand");brandtxt.grid(row=0,column=0)
        brandfield=Entry(win); brandfield.grid(row=0,column=1)

        nametxt=Label(win, text="Name") ; nametxt.grid(row=1,column=0)
        namefield = Entry(win);namefield.grid(row=1,column=1)


        pricetxt = Label(win, text="price"); pricetxt.grid(row=2, column=0)
        pricefield = Entry(win); pricefield.grid(row=2,column=1)

        quanttxt=Label(win, text="Starting Quantity"); quanttxt.grid(row=3, column=0)
        quantityfield = Entry(win); quantityfield.grid(row=3, column=1)

        def add_component():
            conn = sqlite3.connect('stock.db')
            c=conn.cursor()
            c.execute("INSERT INTO stock (brand, name, price, stock) VALUES (?,?,?,?)",(brandfield.get(), namefield.get(), pricefield.get(), quantityfield.get()))
            conn.commit()
            conn.close()
            #clear entry fields 
            brandfield.delete(0,END)
            namefield.delete(0,END)
            pricefield.delete(0,END)
            quantityfield.delete(0,END)

        addbutton = Button(win, text="ADD PRODUCT", command=add_component)
        addbutton.grid(row=4, column=0, columnspan=2)

    def adjust():
        win=Toplevel()
        win.title("Adjust Stock")
        win.geometry("500x500")


        nametxt=Label(win, text="Name") ; nametxt.grid(row=0,column=0)
        namefield = Entry(win);namefield.grid(row=0,column=1)

        quanttxt=Label(win, text="Starting Quantity"); quanttxt.grid(row=1, column=0)
        quantityfield = Entry(win); quantityfield.grid(row=1, column=1)

        def adjust_stock(): 
            conn = sqlite3.connect('stock.db')
            c = conn.cursor()
            c.execute("UPDATE stock SET stock = stock + ? WHERE name = ?",(quantityfield.get(), namefield.get()))
            conn.commit()
            conn.close()
            namefield.delete(0,END)
            quantityfield.delete(0,END)


        adjustbutton=Button(win, text="Adjust Stock Value", command=adjust_stock)
        adjustbutton.grid(row=2,column=0, columnspan=2)

        name1txt=Label(win, text="Name") ; name1txt.grid(row=0,column=2)
        name1field = Entry(win);name1field.grid(row=0,column=3)

        pricetxt=Label(win, text="New Price"); pricetxt.grid(row=1, column=2)
        pricefield=Entry(win); pricefield.grid(row=1, column=3)


        def pricechange():
            conn = sqlite3.connect('stock.db')
            c=conn.cursor()
            c.execute("UPDATE stock SET price = ? WHERE name=?", (pricefield.get(), name1field.get()))
            conn.commit()
            conn.close()

            pricefield.delete(0,END)
            name1field.delete(0,END)

        
        pricebutton = Button(win, text="Change Price", command = pricechange)
        pricebutton.grid(row=2, column=2, columnspan=2)
    
    def component_list():
        win = Toplevel()
        win.geometry("1280x720")


        table = ttk.Treeview(win, columns=("brand","name","price","stock"))
        table.heading("#0", text="")
        table.heading("brand", text="Brand")
        table.heading("name", text="Name")
        table.heading("price", text="Price")
        table.heading("stock", text="Stock")
        table.column("#0", width=0, minwidth=0, stretch=NO)
        table.column("brand", width=150, minwidth=150, stretch=NO)
        table.column("name", width=150, minwidth=150, stretch=NO)
        table.column("price", width=100, minwidth=100, stretch=NO)
        table.column("stock", width=100, minwidth=100, stretch=NO)
        table.pack(expand=True, fill=BOTH)

        def read():
            conn = sqlite3.connect("stock.db")
            c=conn.cursor()

            c.execute("SELECT brand, name, price, stock FROM stock")
            data=c.fetchall()
            c.close()
            conn.close()

            return data

        def populate_table(data):
            for i in table.get_children():
                table.delete(i)

            for item in data:
                table.insert("","end", values=item)
        data=read()
        populate_table(data)
    

    def usedsys():
        win=Toplevel()
        win.title("System Information")

        manufacturer_label = Label(win, text="Manufacturer:",bg="#F18E0F")
        manufacturer_label.grid(row=0, column=0)

        manufacturer_entry = Entry(win)
        manufacturer_entry.grid(row=0, column=1)

        cpu_label = Label(win, text="CPU:",bg="#F18E0F")
        cpu_label.grid(row=1, column=0)

        cpu_entry = Entry(win)
        cpu_entry.grid(row=1, column=1)

        psu_label = Label(win, text="PSU (W):",bg="#F18E0F")
        psu_label.grid(row=2, column=0)

        psu_entry = Entry(win)
        psu_entry.grid(row=2, column=1)

        ram_label = Label(win, text="RAM (GB):",bg="#F18E0F")
        ram_label.grid(row=3, column=0)

        ram_entry = Entry(win)
        ram_entry.grid(row=3, column=1)
        

        def add_system():
            system_info = [manufacturer_entry.get(), cpu_entry.get(), psu_entry.get(), ram_entry.get()]
            sysID = uuid.uuid4()
            fpath = "temp/{}.csv".format(sysID)
            with open(fpath, 'a', newline='') as file:
                writer = csv.writer(file)
                if file.tell() == 0:  # if file is empty, write column headings
                    writer.writerow(["Manufacturer", "CPU", "PSU", "RAM"])
                writer.writerow(system_info)
            manufacturer_entry.delete(0, 'end')
            cpu_entry.delete(0, 'end')
            psu_entry.delete(0, 'end')
            ram_entry.delete(0, 'end')
        add_button = Button(win, text="Add System", command=add_system)
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

    def see_systems():
        sysfiles=glob.glob("temp/*.csv")
        combine=[]
        for i in range(len(sysfiles)):
            df=pd.read_csv(sysfiles[i])
            combine.append(df)
        final = pd.concat(combine)
        #print(final)
        stockwin = Toplevel()
        stockwin.title("Used Systems In Stock")
        table = pt= Table(stockwin, dataframe=final,showtoolbar=True, showstatusbar=True)
        pt.show()


