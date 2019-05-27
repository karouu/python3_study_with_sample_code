# which day of the week
import re
week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def whichDay(c):
	c1 = c.upper()
	result = []
	match = False
	for i in week:
		if re.match(c1, i):         # or i.startswith(c1)
			result.append(i)
	if len(result)==1:
		print(result[0])
		match = True
	else:
		c2 = input('please input second charactre: ')
		c3 = c1+c2
		for i in result:
			if re.match(c3, i):     # or i.startswith(c1)
				print(i)
				match = True
	if not match:	
		print('pls enter correct day')
		
firstChar = input('please input first characer: ')
whichDay(firstChar)


