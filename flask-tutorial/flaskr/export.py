import xlsxwriter
workbook = xlsxwriter.Workbook('FlaskrPosts.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for row_data in rows:
	worksheet.write(row, col, row_data.1)
	worksheet.write(row, col+1, row_data.2)
	row += 1

workbook.close()