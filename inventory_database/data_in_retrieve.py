import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('warehouse.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store the product information
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
''')

# Add a new product to the database
def add_product(name, quantity):
    cursor.execute('''
    INSERT INTO products (name, quantity)
    VALUES (?, ?)
    ''', (name, quantity))
    conn.commit()

# Retrieve the quantity of a product from the database
def get_quantity(name):
    cursor.execute('''
    SELECT quantity FROM products WHERE name=?
    ''', (name,))
    return cursor.fetchone()[0]

# Example usage:
add_product("product1", 10)
print(get_quantity("product1")) # Output: 10
