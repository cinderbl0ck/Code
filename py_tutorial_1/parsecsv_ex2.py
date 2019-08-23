#https://www.youtube.com/watch?v=bkpLhQd6YQM

import csv

html_ouput = ''
names = []

with open('patrons.csv', 'r') as data_file:
	csv_data = csv.DictReader(data_file)

	# We don't want first line of bad data
	next(csv_data)

	for line in csv_data:
		if line['FirstName'] == 'No Reward':
			break
		names.append(f"{line['FirstName']} {line['LastName']}")

html_ouput += f'<p>There are currently {len(names)} public contributors.  Thank You!</p>'

html_ouput += '\n<ul>'

for name in names:
	html_ouput += f'\n\t<li>{name}</li>'

html_ouput += '\n</ul>'

print(html_ouput)