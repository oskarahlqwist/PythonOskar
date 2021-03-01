import sqlite3
conn = sqlite3.connect('sp.db')
cursor = conn.cursor()
cursor.execute('''SELECT * from p ''')

all_rows = cursor.fetchall()
print(all_rows)
print()
print('-------------------------------------')
for row in all_rows:
    print (row)


print('-------------------------------------')
for row in all_rows:
    print (row[0],row[1],row[2],row[3],row[4])
print()
conn.close()
