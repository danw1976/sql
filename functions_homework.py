import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    sql = {'Mustang': "SELECT count(make), make FROM orders WHERE model = 'Mustang'",
           'Cougar': "SELECT count(make), make FROM orders WHERE model = 'Cougar'",
           'Focus': "SELECT count(make), make FROM orders WHERE model = 'Focus'",
           'Civic': "SELECT count(make), make FROM orders WHERE model = 'Civic'",
           'Honda': "SELECT count(make), make FROM orders WHERE model = 'Prelude'"}

    for keys, values in sql.items():

        c.execute(values)

        result = c.fetchone()

        print(result[1] + ' ' + keys)
        print('Order quantity: ' + str(result[0]))

