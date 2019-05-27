# description:check string pattern match etc. 12321, abcbc,level
import os
#s = os.sys.argv[1]
s = '12321'

# best practice
def palindrome1(aStr):
	flag = True
	for i in range(len(aStr)//2):
		if s[i] != s[-i-1]:
			flag = False
			break
	return flag


def palindrome2(aString):
	sList =  list(aString)
	sList.reverse()
	sReverse = ''
	for i in sList:
		sReverse +=i
	
	if s == sReverse:
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
	sList4 = list(s)
	sList4Reverse = sList4[::-1] 
	
	if sList == sList4Reverse:
		return True
	else:
		return False
		
aL = ['palindrome'+str(i) for i in range(1,5)]
print(aL)

#result = [i(str(s)) for i in aL]
#print(result)
for i in aL:
	pass
	
print(palindrome1(s))
f=palindrome1()
f(s)
