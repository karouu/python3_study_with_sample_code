import os
n = int(os.sys.argv[1])

def recursion(n):
	if n == 1:
		return 1
	else:
		return n*recursion(n-1)

print('{}! is {}'.format(n,recursion(n)) )
