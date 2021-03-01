import sqlite3
conn = sqlite3.connect('sp.db')
cursor = conn.cursor()
cursor.execute('''SELECT * from p''')

all_rows = cursor.fetchall()
print()
print('-------------------------------------')
print("%-4s %-8s %-7s %-7s %-8s" % ('PNO', 'PNAME', 'COLOR', 'WEIGHT', 'CITY'))
print('-------------------------------------')
for row in all_rows:
    print ("%-4s %-8s %-7s %-7s %-8s" % (row[0],row[1],row[2],row[3],row[4]))
print()
conn.close()
