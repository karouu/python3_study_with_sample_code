
def prime(n):
	limiter = n//2 +1
	flag = False
	'''
	for i in range(2,n):
		if i**2 > n:
			limiter = i
			break
	'''
	for j in range(2,limiter):
		if n%j == 0:
			return flag
	flag =True
	return flag

n = input('input a number to find prime bumber: ')
for i in range(2,int(n)):
	if prime(i):
		print(i)
