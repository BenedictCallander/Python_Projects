import sqlite3
import tkinter as tk
from tkinter import ttk

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

# Create the main window
disp = tk.Tk()
disp.title("Stock Information")

# Create a table to display the data
table = ttk.Treeview(disp, columns=("name", "price", "stock"))
table.heading("#0", text="")
table.heading("name", text="Name")
table.heading("price", text="Price")
table.heading("stock", text="Stock")
table.column("#0", width=0, minwidth=0, stretch=tk.NO)
table.column("name", width=150, minwidth=150, stretch=tk.NO)
table.column("price", width=100, minwidth=100, stretch=tk.NO)
table.column("stock", width=100, minwidth=100, stretch=tk.NO)
table.pack(expand=True, fill=tk.BOTH)

# Read the data from the database and populate the table
data = read_data_from_db()
populate_table(data)

# Start the main event loop
disp.mainloop()