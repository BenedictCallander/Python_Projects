from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

#
#set up the window

root = Tk()
root.geometry("500x500")
root.resizable(width=False, height=False)

root.title("calculator")

val= ""
A = 0
operator = ""

def entered (event):
    btnc.config(bg="#ff4117")