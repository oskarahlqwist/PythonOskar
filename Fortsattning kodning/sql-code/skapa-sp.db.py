import sqlite3

db = sqlite3.connect('sp.db')
cursor = db.cursor()
#create table s
cursor.execute('''
  create table s (
  sno text,
  sname text,
  status number CHECK (status > 0 and status <= 50),
  city text CHECK (city = 'London' or city = 'Paris' or city = 'Athens' or city = 'Rome' or city = 'Berlin')
  )
''')
db.commit()

#create table sp
cursor.execute('''
create table sp (
  sno text not null,
  pno text not null,
  qty number,
  primary key (sno, pno),
  foreign key (sno) references s (sno),
  foreign key (pno) references p (pno)
)
''')
db.commit()

#create table p
cursor.execute('''
create table p (
  pno text not null primary key,
  pname text,
  color text,
  weight number,
  city text,
  CHECK (color = 'Red' or weight <= 20)
  )
''')
db.commit()

cursor.execute('''insert into s values ('S1','Smith',20,'London')''')
cursor.execute('''insert into s values ('S2','Jones',10,'Paris')''')
cursor.execute('''insert into s values ('S3','Blake',30,'Paris')''')
cursor.execute('''insert into s values ('S4','Clark',20,'London')''')
cursor.execute('''insert into s values ('S5','Adams',30,'Athens')''')
db.commit()

cursor.execute('''insert into p values ('P1','Nut','Red',12,'London')''')
cursor.execute('''insert into p values ('P2','Bolt','Green',17,'Paris')''')
cursor.execute('''insert into p values ('P3','Screw','Blue',17,'Rome')''')
cursor.execute('''insert into p values ('P4','Screw','Red',14,'London')''')
cursor.execute('''insert into p values ('P5','Cam','Blue',12,'Paris')''')
cursor.execute('''insert into p values ('P6','Cog','Red',19,'London')''')
db.commit()

cursor.execute('''insert into sp values ('S1','P1',300)''')
cursor.execute('''insert into sp values ('S1','P2',200)''')
cursor.execute('''insert into sp values ('S1','P3',400)''')
cursor.execute('''insert into sp values ('S1','P4',200)''')
cursor.execute('''insert into sp values ('S1','P5',100)''')
cursor.execute('''insert into sp values ('S1','P6',100)''')
cursor.execute('''insert into sp values ('S2','P1',300)''')
cursor.execute('''insert into sp values ('S2','P2',400)''')
cursor.execute('''insert into sp values ('S3','P2',200)''')
cursor.execute('''insert into sp values ('S4','P2',200)''')
cursor.execute('''insert into sp values ('S4','P4',300)''')
cursor.execute('''insert into sp values ('S4','P5',400)''')
db.commit()
