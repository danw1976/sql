import sqlite3

with sqlite3.connect("numbers.db") as connection:
    c = connection.cursor()

    commands = {1: 'AVG',
                2: 'MAX',
                3: 'MIN',
                4: 'SUM'}

    while True:

        for item, values in commands.items():
            print(str(item) + ': ' + commands[item] + '\n')
            
        command = input("Which operation would you like to perform? ")

        c.execute(f"SELECT {commands[int(command)]}(num) FROM numbers")

        answer = c.fetchone()
        print(answer[0])
