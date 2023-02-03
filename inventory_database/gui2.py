import tkinter as tk
import sqlite3

def add_product():
    # add product to database
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    c.execute("INSERT INTO stock (name, price, stock) VALUES (?, ?, ?)", (entry_name.get(), entry_price.get(), entry_stock.get()))
    conn.commit()
    conn.close()
    # clear entries
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_stock.delete(0, tk.END)

def adjust_stock():
    # update stock level in database
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    c.execute("UPDATE stock SET stock = stock + ? WHERE name = ?", (entry_adjust.get(), entry_name_adjust.get()))
    conn.commit()
    conn.close()
    # clear entries
    entry_name_adjust.delete(0, tk.END)
    entry_adjust.delete(0, tk.END)

# create GUI window
root = tk.Tk()
#root.geometry("500x500")
root.title("Stock Management System")

# create labels and entries for adding product
label_name = tk.Label(root, text="Name")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_price = tk.Label(root, text="Price")
label_price.grid(row=1, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1)

label_stock = tk.Label(root, text="Initial Stock")
label_stock.grid(row=2, column=0)
entry_stock = tk.Entry(root)
entry_stock.grid(row=2, column=1)


# create button for adding product
button_add = tk.Button(root, text="Add Product", command=add_product)
button_add.grid(row=3, column=0, columnspan=2)

# create labels and entries for adjusting stock
label_name_adjust = tk.Label(root, text="Name")
label_name_adjust.grid(row=4, column=0)
entry_name_adjust = tk.Entry(root)
entry_name_adjust.grid(row=4, column=1)

label_adjust = tk.Label(root, text="Adjustment")
label_adjust.grid(row=5, column=0)
entry_adjust = tk.Entry(root)
entry_adjust.grid(row=5, column=1)

# create button for adjusting stock
button_adjust = tk.Button(root, text="Adjust Stock", command=adjust_stock)
button_adjust.grid(row=6, column=0, columnspan=2)

# create database if it does not exist
conn = sqlite3.connect('stock.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS stock (
                    name text,
                    price real,
                    stock integer DEFAULT 0
                )""")
conn.commit()
conn.close()

# start GUI event loop
root.mainloop()