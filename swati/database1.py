import sqlite3

#CONNECTING AND CREATING TABLE IN SQLite via PYTHON
def create():
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT,quantity INTEGER,price REAL)")
	conn.commit()
	conn.close()

#INSERTING DATA INTO DATABASE
def insert(item,quantity,price):
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
	cur.execute("SELECT * FROM store")
	conn.commit()
	conn.close()

#insert("Water Glass",10,8)

#VIEW THE DATA 
def view():
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM store")
	rows=cur.fetchall()
	conn.close()
	return rows

#DELETING RECORDS 
def delete(item):
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM store WHERE item=? ",(item,))
	conn.commit()
	conn.close()
	
#UPDATING RECORDS
def update(price,quantity,item):
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("UPDATE store SET price=?,quantity=? WHERE item=?",(price,quantity,item))
	conn.commit()
	conn.close()

update(11,6,"Water Glass")	
#delete("Water Glass")
print(view())
