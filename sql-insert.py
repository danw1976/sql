import sqlite3
import random

with sqlite3.connect("numbers.db") as connection:
    c = connection.cursor()

    #DROP table if exists
    c.execute("DROP TABLE if exists numbers")

    #CREATE table
    c.execute("CREATE TABLE numbers(num INT)")

    #INSERT 100 random numbers into table
    for x in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0,100),))
