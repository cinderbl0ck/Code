import sqlite3
import xlsxwriter

# Connect / Cursor / Create
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
			first text,
			last text,
			pay integer
			)""")

c.execute("""INSERT INTO employees(first, last, pay)
	VALUES ("Framrod", "KfLablewitz", 80000)""")

print('First user inserted')

c.execute("""INSERT INTO employees(first, last, pay)
	VALUES ("Lemiwinks", "McGee", 60000)""")

print('Second user inserted')
conn.commit()
row = 1

data = c.fetchone()
for row in data:
	print(type(data))
#	row += 1

conn.close()