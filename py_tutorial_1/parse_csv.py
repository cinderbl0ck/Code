#https://www.youtube.com/watch?v=bkpLhQd6YQM

import csv

html_ouput = ''
names = []

with open('patrons.csv', 'r') as data_file:
	csv_data = csv.reader(data_file)

	# We don't want headers or first line of bad data
	next(csv_data)
	next(csv_data)

#	print(list(csv_data))
	for line in csv_data:
		if line[0] == 'No Reward':
			break
		names.append(f"{line[0]} {line[1]}")

html_ouput += f'<p>There are currently {len(names)} public contributors.  Thank You!</p>'

html_ouput += '\n<ul>'

for name in names:
	html_ouput += f'\n\t<li>{name}</li>'

html_ouput += '\n</ul>'

print(html_ouput)
