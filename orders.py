import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE orders
              (make TEXT, model TEXT, order_date TEXT)
              """)

    cars = [
        ('Ford','Mustang','2020-01-01'),
        ('Ford','Mustang','2020-02-03'),
        ('Ford','Mustang','2020-05-02'),
        ('Ford','Cougar','2019-12-19'),
        ('Ford','Cougar','2019-11-11'),
        ('Ford','Cougar','2020-05-04'),
        ('Ford','Focus','2018-08-01'),
        ('Ford','Focus','2019-08-08'),
        ('Ford','Focus','2020-01-05'),
        ('Honda','Civic','2018-05-24'),
        ('Honda','Civic','2019-11-28'),
        ('Honda','Civic','2020-02-18'),
        ('Honda','Prelude','2018-01-19'),
        ('Honda','Prelude','2019-10-12'),
        ('Honda','Prelude','2020-02-15')
    ]

    c.executemany("INSERT INTO orders VALUES(?,?,?)", cars)
