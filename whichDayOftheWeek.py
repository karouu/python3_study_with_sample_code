
# method 1
import os
s = os.sys.argv[1]

if s[0].lower() == 'm':
	print('Monday')
elif s[0].lower() == 'w':
	print('Wednesday')
elif s[0].lower() == 'f':
	print('Friday')
elif s[:2].lower() == 'tu':
	print('Tuesday')
elif s[:2].lower() == 'th':
	print('Thursday')
elif s[:2].lower() == 'sa':
	print('Saturday')
elif s[:2].lower() == 'su':
	print('sunday')

# method 2
import re
week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print('method 2 :')

def whichDay(c):
	c1 = c.upper()
	result = []
	for i in week:
		if re.match(c1,i):   # or i.startswith(c1)
			result.append(i)
	if len(result)==1:
		print(result[0])
	else:
		c2 = input('please input second charactre: ')
		c3 = c1+c2
		for i in result:
			if re.match(c3,i):  # or i.startswith(c1)
				print(i)
	
firstChar = input('please input first characer: ')
whichDay(firstChar)


