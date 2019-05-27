import os
n = int(os.sys.argv[1])
# calculate n!
def factorial(n):
	if n == 1:
		return 1
	else:
		return n*factorial(n-1)

print( '{}! is {}'.format(n, factorial(n)) )


# N(n)=N(n-1)+2, N(1)=10
def N(n):
	if n==1:
		return 10
	else:
		return N(n-1)+2

print('N({}) is {}'.format(n,N(n)))


# input 'abcdefg' output 'gfedcba'
s = input('Input a string: ')

print('\nmethod 1 result')
def output(s, n):
    if n==0:
       return ''
    print(s[n-1], end='')
    output(s, n-1)

output(s, len(s))

print('\nmethod 2 result')
aList = list(s)
aList.reverse()
for i in range(len(aList)):
	print(aList[i], end='')

print('\nmethod 3 result')
for i in range(len(s)-1, -1, -1):
	print(s[i], end='')
print()
