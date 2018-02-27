import os
n = int(os.sys.argv[1])
# n!
def recursion(n):
	if n == 1:
		return 1
	else:
		return n*recursion(n-1)

print( '{}! is {}'.format(n, recursion(n)) )

# N(n)=N(n-1)+2, N(1)=10

def N(n):
	if n==1:
		return 10
	else:
		return N(n-1)+2

print('N({}) is {}'.format(n,N(n)))

# 求0—7所能组成的奇数个数
def f(n):
	if n == 1:
		return 1
	elif n == 2:
		return 7
	else:
		return f(n-1)*8

s = []
for i in range(1,9):
	s.append(f(i)*4)
print(sum(s))