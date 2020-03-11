import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    c.execute("UPDATE inventory SET Quantity = 11 WHERE Model = 'Mustang'")
    c.execute("UPDATE inventory SET Model = 'Fiesta' WHERE Model = 'Escort'")
    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])

