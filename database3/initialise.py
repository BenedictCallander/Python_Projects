import sqlite3

connection = sqlite3.connect("stock.db")
cursor=connection.cursor()

cursor.execute("create table stock (brand text, name text, price integer, stock integer)")


connection.close()