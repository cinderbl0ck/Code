#https://www.youtube.com/watch?v=daefaLgNkw0
student = {'name':  'John', 'age': 25, 'courses': ['Math', 'CompSci']}

#student['phone]'] = '555-5555'
#student['name'] = 'Jane'
#or can do below

#student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

#del student['age']
#age = student.pop('age')

#print(student['courses'])
#print(student.get('phone', 'Not Found')) #returns none instead of error, or error message
#print(student)
#print(age)




#print(len(student))
#print(student.keys())
#print(student.values())
#print(student.items())



#for key in student:
#	print(key)

for key, value in student.items():
	print(key, value)