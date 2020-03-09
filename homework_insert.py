import sqlite3

connection = sqlite3.connect("cars.db")

c = connection.cursor()

cars = ['Ford'
