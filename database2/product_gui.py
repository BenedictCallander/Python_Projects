import tkinter as tk
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("stock.db")
cursor = conn.cursor()

# Create the table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS stock (
    product TEXT,
    price REAL,
    stock INTEGER
)
""")
conn.commit()

# Create the GUI window
root = tk.Tk()
root.title("Warehouse Inventory")

# Create a frame for the product entry fields
entry_frame = tk.Frame(root)
entry_frame.pack()

# Create labels and entry fields for the product name, price, and stock level
product_label = tk.Label(entry_frame, text="Product:")
product_label.grid(row=0, column=0)
product_entry = tk.Entry(entry_frame)
product_entry.grid(row=0, column=1)

price_label = tk.Label(entry_frame, text="Price:")
price_label.grid(row=1, column=0)
price_entry = tk.Entry(entry_frame)
price_entry.grid(row=1, column=1)

stock_label = tk.Label(entry_frame, text="Stock:")
stock_label.grid(row=2, column=0)
stock_entry = tk.Entry(entry_frame)
stock_entry.grid(row=2, column=1)

# Create a function to add a product to the database
def add_product():
    product = product_entry.get()
    price = price_entry.get()
    stock = stock_entry.get()
    cursor.execute("""
    INSERT INTO stock (product, price, stock)
    VALUES (?, ?, ?)
    """, (product, price, stock))
    conn.commit()
    update_list()


# Create a button to add the product to the database
add_button = tk.Button(entry_frame, text="Add Product", command=add_product)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create a frame to display the product list
list_frame = tk.Frame(root)
list_frame.pack()




def update_list():
    for widget in list_frame.winfo_children():
        widget.destroy()
    cursor.execute("SELECT * FROM stock")
    rows = cursor.fetchall()
    for i, row in enumerate(rows):
        product_label = tk.Label(list_frame, text=row[0])
        product_label.grid(row=i, column=0, sticky="W")
        price_label = tk.Label(list_frame, text=row[1])
        price_label.grid(row=i, column=1)
        stock_label = tk.Label(list_frame, text=row[2])
        stock_label.grid(row=i, column=2)


# Call the update_list function to display the initial list of products
update_list()

# Start the GUI event loop
root.mainloop()

# Close the database connection
conn.close()
