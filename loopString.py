# description:string pattern  12321, abcbc,level
import os
s = os.sys.argv[1]

# method 1
sList =  list(s)
sList.reverse()
sReverse = ''
for i in sList:
	sReverse +=i

if s == sReverse:
	print('method 1 result: {} is loop string'.format(s))
else:
	print('method 1 result: {} is not loop string'.format(s))

# method 2
j = len(s)-1
i=0
flag = False
while True:
	if s[i]!=s[j]:
		break
	i += 1
	j -= 1
	if i > j:
		flag = True
		break

if flag == True:
	print('method 2 result: {} is loop string'.format(s))	
else:
	print('method 2 result: {} is not loop string'.format(s))

# method 3 best practice
flag3 = True
for i in range(len(s)//2):
	if s[i] != s[-i-1]:
		flag3 = False
		break

if flag3 == True:
	print('method 3 result: {} is loop string'.format(s))	
else:
	print('method 3 result: {} is not loop string'.format(s))

# method 4 ,smart
sList4 = list(s)
sList4Reverse = sList4[::-1] 

if sList4 == sList4Reverse:
	print('method 4 result: {} is loop string'.format(s))	
else:
	print('method 4 result: {} is not loop string'.format(s))
