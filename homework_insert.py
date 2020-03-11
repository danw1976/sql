import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars = [
        ('Ford', 'Mustang', 10),
        ('Ford', 'Torino', 3),
        ('Ford', 'Escort', 30),
        ('Honda', 'Accord', 12),
        ('Honda', 'Civic', 3)
    ]

    c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", cars)
