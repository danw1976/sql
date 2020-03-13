import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT cars.make, cars.model, cars.quantity,
              orders.order_date FROM cars JOIN orders ON cars.model = orders.model""")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1])
        print(r[2])
        print(r[3],'\n')
        
