import sqlite3
import xlsxwriter

conn = sqlite3.connect('employee.db')

c = conn.cursor()

workbook = xlsxwriter.Workbook('SQL2Excel.xlsx')
worksheet = workbook.add_worksheet('Employees')

# Create Table in code and then comment out after running
#c.execute("""CREATE TABLE employees (
#			first text, 
#			last text, 
#			pay integer 
#			)""")

# Create 2 sample employees and then comment out after running
# c.execute("INSERT INTO employees VALUES ('Lemiwinks', 'McGee', 60000)")

row = 0
col = 0
#item_list = []

c.execute("SELECT * FROM employees")
for item in c.fetchall():
#	item_list.append(item)
	worksheet.write(row, col,   item[0])
	worksheet.write(row, col+1, item[1])
	worksheet.write(row, col+2, item[2])
	row += 1

#print(item_list)
#print(type(item_list))

#for list_data in item_list:
#  worksheet.write(row, col,   list_data[0])
#  worksheet.write(row, col+1, list_data[1])
#  worksheet.write(row, col+2, list_data[2])
#  row += 1

workbook.close()
conn.commit()
conn.close()