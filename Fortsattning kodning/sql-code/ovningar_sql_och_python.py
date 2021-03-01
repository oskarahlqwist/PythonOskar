import sqlite3
conn = sqlite3.connect('sp.db')
cursor = conn.cursor()
cursor.execute('''SELECT * from p ''')

all_rows = cursor.fetchall()
print(all_rows)
print()
for row in all_rows:
    print (row)