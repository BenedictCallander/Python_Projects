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



def testwindow():
    root=Tk()
    root.geometry("1280x720")
    root.title("TEST v1.2")

def main():
    win = Toplevel()
    win.title("delivery")
    win.geometry("1280x720")

    #set title and headers 

    title_main = Label(win, text="Order Input"); title_main.grid(row=0, column=0)
    ramnames = ["4GB PC3", "8GB PC3", "Other PC3", "4GB PC4", "8GB PC4", "16GB PC4", "Other PC4"]
    rvalues = StringVar(ramnames)
    




