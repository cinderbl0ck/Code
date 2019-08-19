# https://www.youtube.com/watch?v=W8KRzm-HUcc
# Lists start at 0 for index position
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']

nums = [1, 5, 2, 4, 3]

# courses.extend(courses_2)
# insert
# append

# popped = courses.pop()
# .remove
# .pop

# (reverse=True)

# courses.sort(reverse=True)
# .reverse
# .sort
# nums.sort(reverse=True)

# sorted_courses = sorted(courses)

# print(popped)
# print(sorted_courses)
# print(min(nums))

# print(courses.index('CompSci'))
# print('Math' in courses)

# for item in courses:
#	print(item)

for index, course in enumerate(courses, start=1):
	print(index, course)























