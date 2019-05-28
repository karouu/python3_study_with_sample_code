# description:check string pattern match etc. 12321, abcbc,level
import os
#s = os.sys.argv[1]
s = 12321

# best practice
def palindrome1(aStr):
	flag = True
	for i in range(len(aStr)//2):
		if aStr[i] != aStr[-i-1]:
			flag = False
			break
	return flag


def palindrome2(aString):
	sList =  list(aString)
	sList.reverse()
	sReverse = ''
	for i in sList:
		sReverse +=i
	
	if aString == sReverse:
		return True
	else:
		return False

def palindrome3(aStr):
	j = len(aStr)-1
	i = 0
	flag = False
	while True:
		if aStr[i]!=aStr[j]:
			break
		i += 1
		j -= 1
		if i >= j:
			flag = True
			break
	return flag


# smart method
def palindrome4(s):
	sList = list(s)
	sList4Reverse = sList[::-1] 
	
	if sList == sList4Reverse:
		return True
	else:
		return False
	
# difference between name and string		
strList = ['palindrome'+str(i) for i in range(1,5)]  
defList = [palindrome1, palindrome2, palindrome3, palindrome4]

#result = [i(str(s)) for i in aL]
#print(result)
for i in defList:
	print( i(str(s)) )
