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




class gpu:
    def __init__(self):
        return 1
    def window(self):
        win = Toplevel()
        win.geometry("500x500")
        win.title("power")
class ram: 
    def __init__(self):
        return 1 
    def window(self):
        win = Toplevel()
        win.geometry("500x500")
        win.title("ram")

class power: 
    def __init__(self):
        return 1 
    def window(self):
        win = Toplevel()
        win.geometry("500x500")
        win.title("power")
class cpu:
    def __init__(self):
        return 1 
    def window(self):
        win = Toplevel()
        win.geometry("500x500")
        win.title("cpu")



def mass_import():
    win= Toplevel()
    win.geometry("1280x720")
    win.title("Component Delivery")

    #LABELS 

    title_header= Label(win, text="Bulk Parts Delivey")
    title_header.grid(row=0, column=0, columnspan=2)



    ram_header = Label(win, text="RAM")
    cpu_header = Label(win, text="CPU")
    power_header=Label(win, text="PSU Wattage")
    ram_header.grid(row=1,column=2); cpu_header.grid(row=1, column= 4); power_header.grid(row=1, column= 6)
    
    '''
    Layout sketch:

    PC3:
        * 4 GB
        * 8 GB
        * Larger/smaller

    PC3:
        * 4 GB
        * 8 GB
        * 16GB
        * Larger
        *Kits (NAME AND BAG SEPARATELY)
    

    '''
