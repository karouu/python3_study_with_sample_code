# N(n)=N(n-1)+2, N(1)=10
import os

def N(n):
	if n==1:
		n=10
	else:
		n=N(n-1)+2
	return n

n =int( os.sys.argv[1])
print('N({}) is {}'.format(n,N(n)))
