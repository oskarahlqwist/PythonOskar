import sqlite3
conn = sqlite3.connect('sp.db')
cursor = conn.cursor()
cursor.execute('''SELECT distinct p.pno from p
               except
               SELECT distinct p.pno from s, sp, p where
               s.sname = 'Jones' and
               s.sno = sp.sno and
               sp.pno = p.pno''')

all_rows = cursor.fetchall()
print()
print('Parts')
print('-----------------')
for row in all_rows:
    print (row[0])
print()
conn.close()
