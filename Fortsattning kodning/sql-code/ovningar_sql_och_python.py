import sqlite3
conn = sqlite3.connect('sp.db')
cursor = conn.cursor()


## 1
cursor.execute('''SELECT sname from s ''')
all_rows = cursor.fetchall()
print('-------------------------------------')
for row in all_rows:
    print (row[0])
print()
conn.close()

##2
cursor.execute('''SELECT pname from p where weight > 14 ''')
all_rows = cursor.fetchall()
print('-------------------------------------')
for row in all_rows:
    print (row[0])
print()
conn.close()

##3
cursor.execute('''Select pname from p where pno in 
(Select pno from sp where sno in (SELECT sno from s where city = "Paris")) ''')
all_rows = cursor.fetchall()
print('-------------------------------------')
for row in all_rows:
    print (row[0])
print()
conn.close()
##4
cursor = conn.cursor()
cursor.execute('''Select sname from s where City ="Athens" ''')
all_rows = cursor.fetchall()
print('-------------------------------------')
for row in all_rows:
    print (row[0])
print()
conn.close()
##5
cursor.execute('''Select sno from s where status between 15 and 25 ''')
all_rows = cursor.fetchall()
print('-------------------------------------')
for row in all_rows:
    print (row[0])
print()
conn.close()

#10