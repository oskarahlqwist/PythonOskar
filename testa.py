import sqlite3
conn = sqlite3.connect('sp.db')
cursor = conn.cursor()

sno = input("För vilken leverantör vill du se antal levererade?: ")

cursor.execute('''Select sum(qty) from sp where sno = &sno ''')
all_rows = cursor.fetchall()
print('-------------------------------------')
for row in all_rows:
    print (row[0])
print()
conn.close()