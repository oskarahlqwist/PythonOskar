##Get suppier names and part numbers for named supplier
import sqlite3
conn = sqlite3.connect('sp.db')
cursor = conn.cursor()
qname = input('Type in a supplier name: ')
cursor.execute('''select distinct sname, pno from s natural join sp where sname = ?''', (qname,)) ##note: comma after qname

all_rows = cursor.fetchall()
print()
print('Supplier    Parts')
print('-----------------')
for row in all_rows:
    print ('%-12s%-10s' % (row[0] ,row[1]))
print()
conn.close()
