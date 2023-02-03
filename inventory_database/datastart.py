import sqlite3

connection = sqlite3.connect("inventory.db")
cursor=connection.cursor()

cursor.execute("create table gpu (model integer, vram integer, city integer)")
list = [
    #gpu, vram, 100
    (1060,6,100),
    (1070,8,100),
    (1080,12,100),
]

cursor.executemany("insert into gpu values (?,?,?)",list)


for row in cursor.execute("select * from gpu"):
    print(row)

connection.close()