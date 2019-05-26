# sum of fractorial: 1+2!+3!+4!+...+n!
import os

n = int(os.sys.argv[1])

# method 1
L = range(1,n+1)
def op(x):
	r  = 1
	for i in range(1,x+1):
		r *= i
	return r

s1 = sum( map(op,L) )
print('sum1 resutl is {}'.format(s1))


# method 2
def sum2(n):
	s2 = 0
	t = 1
	for i in range(1,n+1):
		t *= i
		s2 += t
	return s2
print('sum2 result is {}'.format(sum2(n)))

# method 3
def multi(m):
	result = 1
	for i in range(1,m+1):
		result *= i
	return result	

def sum3(n,m):
	sum = 0
	for i in range(1,n+1):
		sum += m(i)
	return sum

print( 'sum3 result is {}'.format(sum3(n,multi)) )

# method 4
aList = []
for i in range(1,n+1):
	aList.append(multi(i))
sum4 = sum(aList)
print( 'sum4 result is {}'.format(sum4) )





