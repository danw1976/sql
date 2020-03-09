import sqlite3

conn = sqlite3.connect("new_db")

cursor = conn.cursor()

try:
    cursor.execute("insert into populations values('New York City', 'NY', 8400000)")
    cursor.execute("insert into populations values('San Fransisco', 'CA', 800000)")

    conn.commit()
except sqlite3.OperationalError:
    print("Oops! Something went wrong. Try again...")

conn.close()
