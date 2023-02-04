import customtkinter as Ctk
from tkinter import * 
from tkinter import ttk

import sqlite3
#import add_adjust
root=Tk()

def add():
    def add_product():
        # add product to database
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        c.execute("INSERT INTO stock (name, price, stock) VALUES (?, ?, ?)", (entry_name.get(), entry_price.get(), entry_stock.get()))
        conn.commit()
        conn.close()
        # clear entries
        entry_name.delete(0, END)
        entry_price.delete(0, END)
        entry_stock.delete(0, END)
    def adjust_stock():
        # update stock level in database
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        c.execute("UPDATE stock SET stock = stock + ? WHERE name = ?", (entry_adjust.get(), entry_name_adjust.get()))
        conn.commit()
        conn.close()
        # clear entries
        entry_name_adjust.delete(0, END)
        entry_adjust.delete(0, END)

    addwindow = Toplevel()
    addwindow.title("Add Product")
    addwindow.configure(bg="#FA7B19")
    label_name =Label(addwindow, text="Name")
    label_name.grid(row=0, column=0)
    entry_name = Entry(addwindow)
    entry_name.grid(row=0, column=1)

    label_price = Label(addwindow, text="Price")
    label_price.grid(row=1, column=0)
    entry_price = Entry(addwindow)
    entry_price.grid(row=1, column=1)

    label_stock = Label(addwindow, text="Initial Stock")
    label_stock.grid(row=2, column=0)
    entry_stock = Entry(addwindow)
    entry_stock.grid(row=2, column=1)

    button_add = Button(addwindow, text="Add Product", command=add_product)
    button_add.grid(row=3, column=0, columnspan=2)


    label_name_adjust = Label(addwindow, text="Name")
    label_name_adjust.grid(row=4, column=0)
    entry_name_adjust = Entry(addwindow)
    entry_name_adjust.grid(row=4, column=1)

    label_adjust = Label(addwindow, text="Adjustment")
    label_adjust.grid(row=5, column=0)
    entry_adjust = Entry(addwindow)
    entry_adjust.grid(row=5, column=1)

    # create button for adjusting stock
    button_adjust = Button(addwindow, text="Adjust Stock", command=adjust_stock)
    button_adjust.grid(row=6, column=0, columnspan=2)



    closebutton= Button(addwindow, text = "Close", command=addwindow.destroy)
    closebutton.grid(row=7,columnspan=3, padx=20,pady=20)

def adjust():
    win = Toplevel()
    win.title("Adjust Stock")
    win.geometry("500x500")

    def adjust_stock():
        # update stock level in database
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        c.execute("UPDATE stock SET stock = stock + ? WHERE name = ?", (entry_adjust.get(), entry_name_adjust.get()))
        conn.commit()
        conn.close()
        # clear entries
        entry_name_adjust.delete(0, END)
        entry_adjust.delete(0, END)
    label_name_adjust = Label(win, text="Name")
    label_name_adjust.grid(row=0, column=0)
    entry_name_adjust = Entry(win)
    entry_name_adjust.grid(row=0, column=1)

    label_adjust = Label(win, text="Adjustment")
    label_adjust.grid(row=1, column=0)
    entry_adjust = Entry(win)
    entry_adjust.grid(row=1, column=1)

    # create button for adjusting stock
    button_adjust = Button(win, text="Adjust Stock", command=adjust_stock)
    button_adjust.grid(row=2, column=0, columnspan=2)

def adjust_price():
    winP = Toplevel()
    winP.title("Adjust Price")
    winP.geometry("500x500")

    def pricechange():
        # update stock level in database
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        c.execute("UPDATE stock SET price = ? WHERE name = ?", (entry_adjust.get(), entry_name_adjust.get()))
        conn.commit()
        conn.close()
        # clear entries
        entry_name_adjust.delete(0, END)
        entry_adjust.delete(0, END)
    label_name_adjust = Label(winP, text="Name")
    label_name_adjust.grid(row=0, column=0)
    entry_name_adjust = Entry(winP)
    entry_name_adjust.grid(row=0, column=1)

    label_adjust = Label(winP, text="Adjustment")
    label_adjust.grid(row=1, column=0)
    entry_adjust = Entry(winP)
    entry_adjust.grid(row=1, column=1)

    # create button for adjusting stock
    button_adjust = Button(winP, text="Adjust Stock", command=pricechange)
    button_adjust.grid(row=2, column=0, columnspan=2)

def stockcheck():
    disp=Toplevel()
    disp.geometry("500x500")
    def read_data_from_db():
        # Connect to the database file
        conn = sqlite3.connect("stock.db")
        c = conn.cursor()

        # Execute a SELECT statement to retrieve the data
        c.execute("SELECT name, price, stock FROM stock")

        # Fetch the data from the cursor
        data = c.fetchall()

        # Close the cursor and connection
        c.close()
        conn.close()

        return data

    def populate_table(data):
        # Clear the existing rows in the table
        for i in table.get_children():
            table.delete(i)

        # Insert the new data into the table
        for item in data:
            table.insert("", "end", values=item)

    table = ttk.Treeview(disp, columns=("name", "price", "stock"))
    table.heading("#0", text="")
    table.heading("name", text="Name")
    table.heading("price", text="Price")
    table.heading("stock", text="Stock")
    table.column("#0", width=0, minwidth=0, stretch=NO)
    table.column("name", width=150, minwidth=150, stretch=NO)
    table.column("price", width=100, minwidth=100, stretch=NO)
    table.column("stock", width=100, minwidth=100, stretch=NO)
    table.pack(expand=True, fill=BOTH)

# Read the data from the database and populate the table
    data = read_data_from_db()
    populate_table(data)






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

button1 = Button(root, text="Add Stock",bg='red', command=add, padx=50, pady=50)
button2 = Button(root, text="Adjust stock",bg='blue', command= adjust, padx=50, pady=50)
button3 = Button(root, text="Settings",bg='green', padx=50, pady=50)
button4 = Button(root, text="View Inventory",bg='orange',command=stockcheck, padx=50, pady=50)
button5 = Button(root, text="pricechange",bg='#C35F40',command=adjust_price, padx=50, pady=50)
button6 = Button(root, text="Used-sys-import",bg='#F38060',command=adjust_price, padx=50, pady=50)
button1.grid(row=2, column=2)
button2.grid(row=2, column=3)
button3.grid(row=2, column=4)
button4.grid(row=3, column=2)
button5.grid(row=3, column=3)
button6.grid(row=3, column=4)




root.mainloop()


