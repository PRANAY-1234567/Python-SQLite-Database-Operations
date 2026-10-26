'''
import sqlite3 # To create Dummy database   
conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE if not exists python (name varchar(20),age int, address varchar(20))""")
cur.execute("delete from python")  #It will delete the previous data and it will rerun the new data
cur.execute("""INSERT INTO python VALUES ('Pranay', 22, 'Pune')""")
cur.execute("""INSERT INTO python VALUES ('Jignesh', 24, 'Nagar')""")
cur.execute("""INSERT INTO python VALUES ('Raghu', 25, 'Mumbai')""")
conn.commit
res = cur.execute("""SELECT * FROM python WHERE NAME = 'Pranay'""")
for i in res.fetchall():
    print(i)
conn.close()
'''
